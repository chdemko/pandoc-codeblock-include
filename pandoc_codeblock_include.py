#!/usr/bin/env python

"""
Pandoc filter for including file in code block
"""

from panflute import *

def include(elem, doc):
    # Is it a CodeBlock?
    if isinstance(elem, CodeBlock):
        found = False
        start_from = 0
        end_at = -1
        for name, value in elem.attributes.items():
            if name == 'include':
                try:
                    file_content = open(value, 'r').readlines()
                    found = True
                except IOError:
                    debug('[WARNING] pandoc-codeblock-include: ' + value + ' not found')
            elif name == 'startFrom':
                try:
                    start_from = int(value) - 1
                except ValueError:
                    debug('[WARNING] pandoc-codeblock-include: ' + value + ' is not a correct integer')
            elif name == 'endAt':
                try:
                    end_at = int(value)
                except ValueError:
                    debug('[WARNING] pandoc-codeblock-include: ' + value + ' is not a correct integer')
        if found:
            if end_at == -1:
                text = file_content[start_from:]
            else:
                text = file_content[start_from:end_at]
            elem.text = ''.join(text)

            if doc.format in ['latex', 'beamer']:
                # Clear the attributes else latex will get a problem with the listings
                if 'include' in elem.attributes:
                    del elem.attributes['include']
                if 'endAt' in elem.attributes:
                    del elem.attributes['endAt']

def main(doc = None):
    return run_filter(include, doc = doc)

if __name__ == '__main__':
    main()

