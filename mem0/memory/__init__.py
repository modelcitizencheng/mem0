"""Expose memory submodules for convenient external access.

The package originally relied on implicit imports for its submodules, which
meant attributes like ``graph_memory`` were not automatically available when
importing :mod:`mem0.memory`.  Test suites (and user code) expect to access
``mem0.memory.graph_memory`` and ``mem0.memory.telemetry`` directly.  However,
eagerly importing those modules can raise :class:`ImportError` when optional
dependencies are missing.  To keep imports lightweight we lazily load and cache
these submodules on first access.
"""

from __future__ import annotations

import importlib
import types
from typing import Any

__all__ = ["graph_memory", "telemetry"]


def __getattr__(name: str) -> Any:
    """Lazily import submodules when accessed.

    If the real submodule cannot be imported (for example because an optional
    dependency is missing), an empty module is returned so that unit tests can
    mock its contents without triggering import errors.
    """

    if name in __all__:
        try:
            module = importlib.import_module(f"{__name__}.{name}")
        except ImportError:
            module = types.ModuleType(name)
            if name == "graph_memory":
                class _MissingMemoryGraph:  # type: ignore[too-many-ancestors]
                    def __init__(self, *_: Any, **__: Any) -> None:
                        raise ImportError(
                            "graph memory dependencies are not installed"
                        )

                module.MemoryGraph = _MissingMemoryGraph  # type: ignore[attr-defined]
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

