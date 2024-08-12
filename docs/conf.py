# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from __future__ import annotations
import sys
from pathlib import Path

import tomllib

# -- Path setup --------------------------------------------------------------

here = Path(__file__).parent.resolve()
sys.path.insert(0, str(here / ".."))

# -- Project information -----------------------------------------------------

project = "auto_jetbra"
copyright = "2024 Daniil Pavlovich"
author = "Daniil Pavlovich (@vispar-tech)"

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.


def _get_version() -> str:
    with (here / ".." / "pyproject.toml").open("rb") as fp:
        data = tomllib.load(fp)
    version: str = data["tool"]["poetry"]["version"]
    return version


version = _get_version()
release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    ".venv",
    "_build",
]

autodoc_typehints = "description"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"
html_theme_options = {
    "dark_css_variables": {
        "admonition-font-size": "100%",
        "admonition-title-font-size": "100%",
    },
    "light_css_variables": {
        "admonition-font-size": "100%",
        "admonition-title-font-size": "100%",
    },
}
