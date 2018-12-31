#!/usr/bin/env python

"""
Pandoc filter for including file in code block
"""

from panflute import run_filter, debug, CodeBlock


def parse_include(parsed, name, value):
    """
    Extract include information from attributes.

    Arguments
    ---------
        parsed:
            A dictionnary of attributes
        name:
            attribute name
        value:
            attribute value
    """
    if name == "include":
        try:
            file_content = open(value, "r").readlines()
            parsed["content"] = file_content
            parsed["include"] = value
        except IOError:
            debug("[WARNING] pandoc-codeblock-include: " + value + " not found")
        except UnicodeDecodeError:
            debug(
                "[WARNING] pandoc-codeblock-include: file "
                + value
                + " is not encoded in utf-8"
            )


def parse_start_from(parsed, name, value):
    """
    Extract startFrom information from attributes.

    Arguments
    ---------
        parsed:
            A dictionnary of attributes
        name:
            attribute name
        value:
            attribute value
    """
    if name == "startFrom":
        try:
            parsed["start_from"] = int(value) - 1
        except ValueError:
            debug(
                "[WARNING] pandoc-codeblock-include: "
                + value
                + " is not a correct integer"
            )


def parse_end_at(parsed, name, value):
    """
    Extract entAt information from attributes.

    Arguments
    ---------
        parsed:
            A dictionnary of attributes
        name:
            attribute name
        value:
            attribute value
    """
    if name == "endAt":
        try:
            parsed["end_at"] = int(value)
        except ValueError:
            debug(
                "[WARNING] pandoc-codeblock-include: "
                + value
                + " is not a correct integer"
            )


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
        parse_include(parsed, name, value)
        parse_start_from(parsed, name, value)
        parse_end_at(parsed, name, value)
    return parsed


def inject_content(elem, parsed):
    """
    Inject parsed attributes into element content.

    Arguments
    ---------
        elem:
            Pandoc element
        parsed:
            dictionnary of attributes
    """
    start_from = parsed.get("start_from", 0)
    end_at = parsed.get("end_at", len(parsed["content"]))
    text = parsed["content"][start_from:end_at]

    # inject file content in element text
    try:
        elem.text = "".join(line.decode("utf8") for line in text)
    except AttributeError:
        elem.text = "".join(text)
    except UnicodeDecodeError:
        debug(
            "[WARNING] pandoc-codeblock-include: file "
            + parsed["include"]
            + " is not encoded in utf-8"
        )


def clear_latex_attributes(elem):
    """
    Clear LaTeX attributes.

    Arguments
    ---------
        elem:
            current element
    """
    # Clear the attributes else latex will get a problem with the listings
    for attribute in ["include", "endAt"]:
        if attribute in elem.attributes:
            del elem.attributes[attribute]


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
        if "content" in parsed:
            inject_content(elem, parsed)
        if doc.format in ["latex", "beamer"]:
            clear_latex_attributes(elem)


def main(doc=None):
    """
    main function.

    Arguments
    ---------
        doc:
            pandoc document
    """
    return run_filter(include, doc=doc)


if __name__ == "__main__":
    main()
