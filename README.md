# pandoc-codeblock-include
[![Build Status](https://img.shields.io/travis/chdemko/pandoc-codeblock-include/master.svg?logo=travis)](https://travis-ci.org/chdemko/pandoc-codeblock-include/branches)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-codeblock-include/master.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-codeblock-include?branch=master)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-codeblock-include.svg?logo=scrutinizer)](https://scrutinizer-ci.com/g/chdemko/pandoc-codeblock-include/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-codeblock-include.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-codeblock-include/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-codeblock-include.svg)](https://pypi.org/project/pandoc-codeblock-include/)
[![License](https://img.shields.io/pypi/l/pandoc-codeblock-include.svg?colorA=ffffff&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gwPESoBD0PYhwAAAylJREFUKBUBHgPh/AAAAAAAAAAAAAAAAADVl5UAAAAAAAAAAADHc3ETvFRSj71WVH8AAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAANKZmAAraWsA////B7lKR37pwsHT79XUcPv09AIAAAAA8YeSOPBRYlYAAAAAAAAAAAEAAAAAwmRjAD6cnQDFb2097cnJsfrz8hEAAAAAAP//ABEpKos06P4K+87YawAAAQACIBjHCoV6UQEAAAAAv1tZMPjs7Hz25uVT//39AAAAAAACBAQABQ4OxSgOG7ISzd9o//P2IQD+/wAA//4AAhgUAAG6T02i9ODfVP77+wkAAQEA//39AAcREecNIiJjKGZowBk/QPfwSV8R//j3W/7O14oA+fsJABINAAL04N9d/vz8CQABAQADCAj2ESoqiU7HyhpBpai34rSz9wAAAAADNSvvthj4ncowEODrEQQA/gIBAAQAAQEAAP//AAQMCwAYOjwoOJCS4wAAAADw29sAECUlAAAAAADrMCMAE8/BAfr9/P/RFPwAFAgCAAIO/gUA/gD/AAMFBwA4kJLjAAAAAAAAAAAQJSUAAAAAAIgAAAAiUlMAH01OIQEAASAD/gAA9AP9AAIz4fwAKPAEAAr8AAAAAAAAAAAAAOu7vQAAAAAAAAAAAEFxbyS5S0mU1pOR1Pju7QoA//8AAAAAAAHtEC7/APj6APsIAwAGEhGeEd3DbwEBAfQAAAAAuElGivbo6GP++voSAAAAAP/9/QAHEhL8DiUmaQHtEy/z//b5DAAAAAAA/v4AAhsUAPE+LWnS2M5/+/LyGAABAQAAAAAAAQMD9wsdHrNItbdXAAAAAAIFYFIzAiIdoQAIBAABEg/mAwsKausPCB/68PAYAAAAAAEBAQAIEhKvFDI0R0i1t1cAAAAAAAAAAAIOjX/a/R8aYghuYSQFd2YvD9O8l/r8++sA//8ABxAQ7h9TVEcLHRtTP6ChwzYAAADMh4YAAAAAAAAAAAAA+b3FAAAAAAAAAAAAAAAAAMl5d2m4TEmQAAAAAAAAAADMf30AAAAAAAAAAAAAAAAAAAAAAJHc+Cs/L6tDAAAAAElFTkSuQmCC
)](https://raw.githubusercontent.com/chdemko/pandoc-codeblock-include/master/LICENSE)
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

To upgrade to the current code, use

    pip install --upgrade --force git+https://github.com/chdemko/pandoc-codeblock-include

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

