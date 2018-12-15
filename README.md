# pandoc-codeblock-include
[![Build Status](https://img.shields.io/travis/chdemko/pandoc-codeblock-include/master.svg?logo=travis)](https://travis-ci.org/chdemko/pandoc-codeblock-include/branches)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-codeblock-include/master.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-codeblock-include?branch=master)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-codeblock-include.svg?logo=scrutinizer)](https://scrutinizer-ci.com/g/chdemko/pandoc-codeblock-include/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-codeblock-include.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-codeblock-include/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-codeblock-include.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAgCAYAAAAIXrg4AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAChSURBVEiJ7ZRRCsIwEERnpVew4A08Rw/uIaygN+gtfP5sRa01kGwKQuYr2ZB9TCaJAShGN0mDmU2vxV1Qc0k6SjoBh7cqrtyuvv0OXHw8An0NwB44+/z6dBIF8PESEgnwee/HBDDa3NzMLBfwaz3yFn1VV9pgzfnsrLqD/wcsMij9mz4z2d5B7ntYU8sgqZZB0nHLoAEaYAOAlf6eKVV38AAQiKbtcu2AoQAAAABJRU5ErkJggg==)](https://pypi.org/project/pandoc-codeblock-include/)
[![License](https://img.shields.io/pypi/l/pandoc-codeblock-include.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABQCAYAAADvCdDvAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAARYSURBVHic7Z09iB1VGIafb9hEjIqaVVT8KSJRAiaFGi201ErMRm0kwUYFQSE2hiTG0p/4U9gYxMJCxELQuCGFhUIEFWFNoRgFA1oYU8Q/TDYWieS1mHsv6+7snb8z956953uqy8yZ77wzL+fMnG/O3GMUIGkVMANsBW4DrgcuKirrVGYeOA4cAT4CZs3s3OJCtniDpBngVWB91woT5xiw08xmF27M+j8kZZJeInfPzeie9cABSS9KGvgwtaDAC8DukctKGwP29H4/29/Q76YOUNCFOSNBwFYzO2i9G/hRvJsaNz8BGzLypyk3Y/ysA7ZkwAPjVuIMmMmA28etwhmw2SSdBi4etxIHgHmTpColzcyfwFpQ9Tpn5UWcUeKGRIYbEhluSGS4IZHhhkSGGxIZbkhkuCGRMVVepB6SdoWOuRgzezlULEnrgM3AleTzBs4AJ4E5M/s5VD11BFUidLw2BDhnk7Rd0g8lVX0vaZuk1mmjqucWPJcV4oKF0lKE8hdy75PPqKnKh8DDRbNEatTruaxl2E89MwAeBN7oQMsSkmohku4AvqLZ3AEBd5rZXMO6vYUUsIPmEzkMeCqgluJKUmkhkqbIn54ub1H1H8DVZvZvg/q9hSziJtqZATAN3BhAy7KkZMjNkcUpJPjAEAg2aAvMNYHiXBsoTiHBDTGzWKejhprI0elXACl1WasDxbkgUJxCUjLkr0Bx/gwUp5CUDPk9UJzfAsUpJCVDfgkU53igOIV0MTCMMv0uaTX5wK7Nzf00MN0kyVj5OqcyUgeQdAi4r0XVh8zs/oZ1+0i9gLdaHv9mEBVDSK2FZMB3wIYGhx8FNppZo/PzFlKAmZ0HniRPpdfl6aZm1CEpQwDM7DDwbs3D3jGzTzuQs4Skuqw+ki4FvgVuqFD8V/KuqtXA0rusIZjZ38BjlHddAh5va0YdkjQEwMw+IZ+8MIwPzOzjUejpk1L6vYj9wEND9o9kYsNCkv6kTdJa8tH7cqwN1V35PaQaq0r2d9GDDCV1Q7a33B+eqlMcRy6sYyRtkvRPyWmfkbQxUH2VSLKFSLoXOAxcWFJ0DfCZpHs6F9UjmfQ7gKSrgOeBR6nXXZ8H3gb2mtnJhnV7+r2PpFuBJ4BHKG8VwzgLzAKvm9mXNTW4IZK2AbuATR3I+AZ4xczeq6jFDZH0OXBXh1K+MLO7K2rxcQhwRcfxp0MHnHRDLltp8SfdkDUrLf6kG1KWGoku/qQb0nUuKnj8SU+/v0a3f30b/Iky6fT7KPHH3hWKGxIZbkhkuCGR4YZEhhsSGW5IZLghkeGGRIZJOgVcMm4hDgCnMuDEuFU4A05kwNfjVuEMmMvIl8lz4sAXBYuIH4Fbst431zvpILfvVEbkq36eywB6y3/G9GIpNfaZ2UH4/xvDveRO7cYXmBwVAvYBz/U3FC1OvIX81affU7rlGPBMv2X0KWwJWrp893X4Sm5tmSf/A5wj5PODC5fv/g/YY81BSz6WxQAAAABJRU5ErkJggg==)](https://raw.githubusercontent.com/chdemko/pandoc-codeblock-include/master/LICENSE)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-codeblock-include.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-codeblock-include/)
[![Development Status](https://img.shields.io/pypi/status/pandoc-codeblock-include.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAQCAYAAAAI0W+oAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAABmSURBVDiNY/z///9/BhoBRkZGRhibiVaWoAMWJLY0Fc19ii7ACAs6RkZGRmzBSIk4ctCxoCukNoBZSrc4GrVo1CL6W0TzfATLtCzYBHEpJlYcG4Bb9P///2fEaiIHYC2vqGY4ko8BaSAlF2eaBq8AAAAASUVORK5CYII=)](https://pypi.org/project/pandoc-codeblock-include/) ficense icon by [Daniel Bruce](https://www.iconfinder.com/icons/216659/license_icon), format icon by [Picol](https://www.iconfinder.com/icons/103509/document_text_icon), status icon by [iconnice studio](https://www.iconfinder.com/icons/1041629/battery_battery_status_full_full_battery_icon)

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

