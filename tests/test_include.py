"""
Test pandoc-codeblock-include filter.
"""

from os import path
from pathlib import Path
from unittest import TestCase

from panflute import convert_text

from pandoc_codeblock_include import main


class IncludeTest(TestCase):
    """
    Test pandoc-codeblock-include filter.
    """

    @staticmethod
    def scenario():
        """
        Get all tests

        Returns
        -------
            A list of all tests.
        """
        return [
            ("content1.md", "markdown", "expected1.md"),
            ("content2.md", "markdown", "expected2.md"),
            ("content3.md", "markdown", "expected3.md"),
            ("content4.md", "latex", "expected4.md"),
            ("content5.md", "markdown", "expected5.md"),
            ("content6.md", "markdown", "expected6.md"),
        ]

    def test_include(self):
        """
        Test include function (via main).
        """
        for content, output, expected in IncludeTest.scenario():
            folder = path.abspath(path.dirname(__file__))
            content_text = Path(path.join(folder, content)).read_text()
            expected_text = Path(path.join(folder, expected)).read_text()

            doc = convert_text(content_text, standalone=True)
            doc.format = output

            self.assertEqual(
                convert_text(
                    main(doc),
                    standalone=True,
                    input_format="panflute",
                    output_format="markdown",
                ),
                expected_text,
                "Error in converting "
                + content
                + " to "
                + expected
                + " with format "
                + output,
            )
