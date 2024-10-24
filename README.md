Installation
============

[![Python package](https://github.com/chdemko/pandoc-codeblock-include/workflows/Python%20package/badge.svg?branch=develop)](https://github.com/chdemko/pandoc-codeblock-include/actions/workflows/python-package.yml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-codeblock-include/develop.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-codeblock-include?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-codeblock-include.svg?logo=scrutinizer)](https://scrutinizer-ci.com/g/chdemko/pandoc-codeblock-include/)
[![Code Climate](https://codeclimate.com/github/chdemko/pandoc-codeblock-include/badges/gpa.svg)](https://codeclimate.com/github/chdemko/pandoc-codeblock-include/)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/chdemko/pandoc-codeblock-include/develop.svg?logo=codefactor)](https://www.codefactor.io/repository/github/chdemko/pandoc-codeblock-include)
[![Codacy](https://img.shields.io/codacy/grade/26716ef242ba4089aff55eff7ca592a9.svg?logo=codacy&logoColor=white)](https://app.codacy.com/gh/chdemko/pandoc-codeblock-include/dashboard)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-codeblock-include.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-codeblock-include/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-codeblock-include.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-codeblock-include/)
[![License](https://img.shields.io/pypi/l/pandoc-codeblock-include.svg?logo=pypi&logoColor=white)](https://raw.githubusercontent.com/chdemko/pandoc-codeblock-include/develop/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-codeblock-include?logo=pypi&logoColor=white)](https://pepy.tech/project/pandoc-codeblock-include)
[![Development Status](https://img.shields.io/pypi/status/pandoc-codeblock-include.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-codeblock-include/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-codeblock-include.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-codeblock-include/)
[![Pandoc version](https://img.shields.io/badge/pandoc-2.11%20|%202.12%20|%202.13%20|%202.14%20|%202.15%20|%202.16%20|%202.17%20|%202.18%20|%202.19%20|%203.0%20|%203.1%20|%203.2%20|%203.3%20|%203.4%20|%203.5-blue.svg?logo=markdown)](https://pandoc.org/)
[![Latest release](https://img.shields.io/github/release-date/chdemko/pandoc-codeblock-include.svg?logo=github)](https://github.com/chdemko/pandoc-codeblock-include/releases)
[![Last commit](https://img.shields.io/github/last-commit/chdemko/pandoc-codeblock-include/develop?logo=github)](https://github.com/chdemko/pandoc-codeblock-include/commit/develop/)
[![Repo Size](https://img.shields.io/github/repo-size/chdemko/pandoc-codeblock-include.svg?logo=github)](http://pandoc-codeblock-include.readthedocs.io/en/latest/)
[![Code Size](https://img.shields.io/github/languages/code-size/chdemko/pandoc-codeblock-include.svg?logo=github)](http://pandoc-codeblock-include.readthedocs.io/en/latest/)
[![Source Rank](https://img.shields.io/librariesio/sourcerank/pypi/pandoc-codeblock-include.svg?logo=libraries.io&logoColor=white)](https://libraries.io/pypi/pandoc-codeblock-include)
[![Docs](https://img.shields.io/readthedocs/pandoc-codeblock-include.svg?logo=read-the-docs&logoColor=white)](https://pandoc-codeblock-include.readthedocs.io)

*pandoc-codeblock-include* is a [pandoc] filter for including files in
`CodeBlock` elements.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-codeblock-include* requires [python], a programming language that
comes pre-installed on linux and Mac OS X, and which is easily installed
[on Windows].

Install *pandoc-codeblock-include* using the bash command

~~~shell-session
$ pipx install pandoc-codeblock-include
~~~

To upgrade to the most recent release, use

~~~shell-session
$ pipx upgrade pandoc-codeblock-include
~~~

`pipx` is a script to install and run python applications in isolated
environments from the Python Package Index, [PyPI]. It can be installed
using instructions given [here](https://pipx.pypa.io/stable/).

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with *pandoc-codeblock-include*, please feel
welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-codeblock-include/issues

Contribute
==========

Instructions
------------

Install `hatch`, then run

~~~shell-session
$ hatch run pip install pre-commit
$ hatch run pre-commit install
~~~

to install `pre-commit` before working on your changes.

Tests
-----

When your changes are ready, run

~~~shell-session
$ hatch test
$ hatch fmt --check
$ hatch run lint:check
$ hatch run docs:build
$ hatch build -t wheel
~~~

for running the tests, checking the style, building the documentation
and building the wheel.

