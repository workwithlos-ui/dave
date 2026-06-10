"""DAVE, Data Acquisition and Validation Engine.

DAVE is an async-first library for turning web pages into validated structured data.
"""

from __future__ import annotations

from typing import Any, TypeVar

from pydantic import BaseModel

from dave import recipes
from dave.core.config import DaveConfig
from dave.core.engine import CostEstimate, DaveEngine, DaveExtraction, StreamEvent

__all__ = [
    "CostEstimate",
    "DaveConfig",
    "DaveEngine",
    "DaveExtraction",
    "StreamEvent",
    "extract",
    "extract_sync",
    "recipes",
]

T = TypeVar("T", bound=BaseModel)


async def extract(
    url: str,
    schema_or_prompt: type[T] | str | None = None,
    *,
    prompt: str | None = None,
    config: DaveConfig | None = None,
    **kwargs: Any,
) -> T | dict[str, Any] | DaveExtraction:
    """Extract structured data from a URL.

    Calling this with only a URL activates zero-config extraction. DAVE infers the most important page data.
    """
    engine = DaveEngine(config=config)
    return await engine.extract(url, schema_or_prompt, prompt=prompt, **kwargs)


def extract_sync(
    url: str,
    schema_or_prompt: type[T] | str | None = None,
    *,
    prompt: str | None = None,
    config: DaveConfig | None = None,
    **kwargs: Any,
) -> T | dict[str, Any] | DaveExtraction:
    """Synchronous wrapper around :func:`extract`."""
    engine = DaveEngine(config=config)
    return engine.extract_sync(url, schema_or_prompt, prompt=prompt, **kwargs)
