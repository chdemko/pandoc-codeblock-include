#!/usr/bin/env python

"""
Pandoc filter for including file in code block.
"""

from collections.abc import Iterable
from typing import Any

from panflute import CodeBlock, Doc, Element, debug, run_filters


def parse_include(parsed: dict[str, Any], name: str, value: str) -> None:
    """
    Extract include information from attributes.

    Arguments
    ---------
    parsed
        A dictionnary of attributes
    name
        attribute name
    value
        attribute value
    """
    if name == "include":
        try:
            with open(value, encoding="utf-8") as stream:
                file_content = stream.readlines()
            parsed["content"] = file_content
            parsed["include"] = value
        except OSError:
            debug("[WARNING] pandoc-codeblock-include: " + value + " not found")
        except UnicodeDecodeError:
            debug(
                "[WARNING] pandoc-codeblock-include: file "
                + value
                + " is not encoded in utf-8"
            )


def parse_start_from(parsed: dict[str, Any], name: str, value: str) -> None:
    """
    Extract startFrom information from attributes.

    Arguments
    ---------
    parsed
        A dictionnary of attributes
    name
        attribute name
    value
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


def parse_end_at(parsed: dict[str, Any], name: str, value: str) -> None:
    """
    Extract information from attributes.

    Arguments
    ---------
    parsed
        A dictionnary of attributes
    name
        attribute name
    value
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


def parse_attributes(items: Iterable[tuple[str, str]]) -> dict[str, str]:
    """
    Extract usefull information from attributes.

    Arguments
    ---------
    items
        element attributes

    Returns
    -------
    dict[str, str]
        a mapping containing possible 'content', 'start_from' and 'end_at'
    """
    parsed: dict[str, Any] = {}
    for name, value in items:
        parse_include(parsed, name, value)
        parse_start_from(parsed, name, value)
        parse_end_at(parsed, name, value)
    return parsed


def inject_content(elem: Element, parsed: dict[str, Any]) -> None:
    """
    Inject parsed attributes into element content.

    Arguments
    ---------
    elem
        Pandoc element
    parsed
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


def clear_latex_attributes(elem: Element) -> None:
    """
    Clear LaTeX attributes.

    Arguments
    ---------
    elem
        current element
    """
    # Clear the attributes else latex will get a problem with the listings
    for attribute in ("include", "endAt"):
        if attribute in elem.attributes:
            del elem.attributes[attribute]


def include(elem: Element, doc: Doc) -> None:
    """
    Transform CodeBlock element.

    Arguments
    ---------
    elem
        current element
    doc
        pandoc document
    """
    # Is it a CodeBlock?
    if isinstance(elem, CodeBlock):
        parsed = parse_attributes(elem.attributes.items())
        if "content" in parsed:
            inject_content(elem, parsed)
        if doc.format in ("latex", "beamer"):
            clear_latex_attributes(elem)


def main(doc: Doc | None = None) -> Doc:
    """
    Convert the pandoc document.

    Arguments
    ---------
    doc
        pandoc document

    Returns
    -------
    Doc
        The modified pandoc document.
    """
    return run_filters([include], doc=doc)


if __name__ == "__main__":
    main()
