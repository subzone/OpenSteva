"""OpenSteva — modular AI assistant backend with composable intelligence primitives."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version

from opensteva.sdk import Steva, StevaSystem, MemoryHandle, SystemBuilder

try:
    __version__ = _pkg_version("opensteva")
except PackageNotFoundError:  # pragma: no cover — uninstalled source tree
    __version__ = "0.0.0+unknown"

__all__ = ["Steva", "StevaSystem", "MemoryHandle", "SystemBuilder", "__version__"]
