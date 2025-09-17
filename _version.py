"""Runtime helpers for exposing the package version.

This module intentionally avoids build-time rewriting so that editable
installs stay clean. When the package metadata is available we rely on
importlib.metadata to provide the canonical version string.
"""

from __future__ import annotations

from importlib import metadata

__all__ = [
    "__version__",
    "__version_tuple__",
    "version",
    "version_tuple",
    "__commit_id__",
    "commit_id",
]

_PACKAGE_NAME = "pywhispercpp"


def _read_version() -> str:
    try:
        return metadata.version(_PACKAGE_NAME)
    except metadata.PackageNotFoundError:
        return "0.0.0"


def _version_tuple(ver: str) -> tuple:
    parts: list = []
    for token in ver.replace("+", ".").split("."):
        if not token:
            continue
        parts.append(int(token) if token.isdigit() else token)
    return tuple(parts)


def _commit_id(ver: str) -> str:
    if "+" not in ver:
        return ""
    local = ver.split("+", 1)[1]
    for token in local.replace("-", ".").split("."):
        if token.startswith("g") and len(token) >= 8:
            return token
    return ""


version = __version__ = _read_version()
version_tuple = __version_tuple__ = _version_tuple(__version__)
commit_id = __commit_id__ = _commit_id(__version__)
