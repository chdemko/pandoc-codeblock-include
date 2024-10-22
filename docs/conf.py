"""The configuration module for sphinx."""

import datetime
import os
import sys
from pathlib import Path

import tomllib

with Path("..", "pyproject.toml").resolve().open("rb") as f:
    data = tomllib.load(f)
    project = data["project"]["name"]
    author = ",".join(author["name"] for author in data["project"]["authors"])
version = os.popen("hatch version").readline().strip()  # noqa: S605, S607
year = datetime.datetime.now(tz=datetime.UTC).date().year
# noinspection PyShadowingBuiltins
copyright = f"2019-{year}, {author}"  # noqa: A001

python_path = str(Path("..").resolve())
sys.path.insert(0, python_path)
os.environ["PYTHONPATH"] = python_path

on_rtd = os.environ.get("READTHEDOCS") == "True"


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = "8.1"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["myst_parser", "sphinx_copybutton"]

copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_line_continuation_character = "\\"

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}


# The master document.
master_doc = "index"

# The language for content generated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["images"]

# The name of the syntax highlighting style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.
#
# html_sidebars = {}
