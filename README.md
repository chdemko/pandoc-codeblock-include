# pandoc-codeblock-include
[![Build Status](https://img.shields.io/travis/chdemko/pandoc-codeblock-include/0.0.2.svg)](https://travis-ci.org/chdemko/pandoc-codeblock-include/branches)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-codeblock-include/0.0.2.svg)](https://coveralls.io/github/chdemko/pandoc-codeblock-include?branch=0.0.2)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-codeblock-include.svg)](https://scrutinizer-ci.com/g/chdemko/pandoc-codeblock-include/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-codeblock-include.svg)](https://pypi.org/project/pandoc-codeblock-include/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-codeblock-include/0.0.2.svg)](https://pypi.org/project/pandoc-codeblock-include/0.0.2/)
[![License](https://img.shields.io/pypi/l/pandoc-codeblock-include/0.0.2.svg)](https://raw.githubusercontent.com/chdemko/pandoc-codeblock-include/0.0.2/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-codeblock-include.svg)](https://pypi.org/project/pandoc-codeblock-include/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-codeblock-include.svg)](https://pypi.org/project/pandoc-codeblock-include/)
[![Development Status](https://img.shields.io/pypi/status/pandoc-codeblock-include.svg)](https://pypi.org/project/pandoc-codeblock-include/)

*pandoc-codeblock-include* is a [pandoc] filter for including files in `CodeBlock` elements.

[pandoc]: http://pandoc.org/

Documentation
-------------

See the [wiki pages](https://github.com/chdemko/pandoc-codeblock-include/wiki).

Usage
-----

To apply the filter, use the following option with pandoc:

    --filter pandoc-codeblock-include

Installation
------------

*pandoc-codeblock-include* requires [python], a programming language that comes pre-installed on linux and Mac OS X, and which is easily installed [on Windows]. Either python 2.7 or 3.x will do.

Install *pandoc-codeblock-include* as root using the bash command

    pip install pandoc-codeblock-include

To upgrade to the most recent release, use

    pip install --upgrade pandoc-codeblock-include

`pip` is a script that downloads and installs modules from the Python Package Index, [PyPI].  It should come installed with your python distribution. If you are running linux, `pip` may be bundled separately. On a Debian-based system (including Ubuntu), you can install it as root using

    apt-get update
    apt-get install python-pip

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with *pandoc-codeblock-include*, please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-codeblock-include/issues

