Usage
=====

To apply the filter, use the following option with pandoc:

~~~shell-session
$ pandoc --filter pandoc-codeblock-include
~~~

Explanation
-----------

In the attributes of a `CodeBlock` element, you can specify an file
to be included and the start and end lines using attributes:

* `include` for the path of the included file
* `startFrom` for the first line to include
* `endAt` for the last line to include

Example
-------

Demonstration: Using [pandoc-codeblock-include-sample.txt] as input gives
output file in [pdf] (use [lorem] content).

[pandoc-codeblock-include-sample.txt]: https://raw.githubusercontent.com/chdemko/pandoc-codeblock-include/develop/docs/images/pandoc-codeblock-include-sample.txt
[lorem]: https://raw.githubusercontent.com/chdemko/pandoc-codeblock-include/develop/docs/images/lorem
[pdf]: https://raw.githubusercontent.com/chdemko/pandoc-codeblock-include/develop/docs/images/pandoc-codeblock-include-sample.pdf
