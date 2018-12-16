#!/usr/bin/env python

"""
Pandoc filter for including file in code block
"""

from panflute import run_filter, debug, CodeBlock

def parse_attributes(items):
    """
    Extract usefull information from attributes.

    Arguments
    ---------
        items:
            element attributes

    Returns
    -------
        a mapping containing possible 'content', 'start_from' and 'end_at'
    """
    parsed = {}
    for name, value in items:
        if name == 'include':
            try:
                file_content = open(value, 'r').readlines()
                parsed['content'] = file_content
                parsed['include'] = value
            except IOError:
                debug(
                    '[WARNING] pandoc-codeblock-include: '
                    + value
                    + ' not found'
                )
            except UnicodeDecodeError:
                debug(
                    '[WARNING] pandoc-codeblock-include: file '
                    + value
                    + ' is not encoded in utf-8'
                )

        elif name == 'startFrom':
            try:
                parsed['start_from'] = int(value) - 1
            except ValueError:
                debug(
                    '[WARNING] pandoc-codeblock-include: '
                    + value
                    + ' is not a correct integer'
                )
        elif name == 'endAt':
            try:
                parsed['end_at'] = int(value)
            except ValueError:
                debug(
                    '[WARNING] pandoc-codeblock-include: '
                    + value
                    + ' is not a correct integer'
                )

    return parsed


def include(elem, doc):
    """
    Transform CodeBlock element.

    Arguments
    ---------
        elem:
            current element
        doc:
            pandoc document
    """
    # Is it a CodeBlock?
    if isinstance(elem, CodeBlock):

        parsed = parse_attributes(elem.attributes.items())

        if 'content' in parsed:
            start_from = parsed.get('start_from', 0)
            end_at = parsed.get('end_at', len(parsed['content']))
            text = parsed['content'][start_from:end_at]

            # inject file content in element text
            try:
                elem.text = ''.join(line.decode('utf8') for line in text)
            except AttributeError:
                elem.text = ''.join(text)
            except UnicodeDecodeError:
                debug(
                    '[WARNING] pandoc-codeblock-include: file '
                    + parsed['include']
                    + ' is not encoded in utf-8'
                )

        if doc.format in ['latex', 'beamer']:
            # Clear the attributes else latex will get a problem with the listings
            if 'include' in elem.attributes:
                del elem.attributes['include']
            if 'endAt' in elem.attributes:
                del elem.attributes['endAt']


def main(doc=None):
    """
    main function.

    Arguments
    ---------
        doc:
            pandoc document
    """
    return run_filter(include, doc=doc)

if __name__ == '__main__':
    main()
