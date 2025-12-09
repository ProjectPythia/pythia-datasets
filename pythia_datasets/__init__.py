#!/usr/bin/env python3
# flake8: noqa
"""Top-level module for pythia-datasets ."""
from importlib.metadata import version as _version

from .datasets import DATASETS, locate

try:
    __version__ = _version(__name__)
except Exception:  # pragma: no cover
    # package is not installed
    __version__ = 'unknown'  # pragma: no cover
