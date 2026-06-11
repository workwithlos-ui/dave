"""DAVE, Data Acquisition and Validation Engine.

DAVE is an async-first library for turning web pages into validated structured data.
"""

from __future__ import annotations

from typing import Any, TypeVar

from pydantic import BaseModel

from dave import recipes
from dave.core.config import DaveConfig
from dave.core.engine import CostEstimate, DaveEngine, DaveExtraction, StreamEvent
from dave.search import BaseSearchProvider, SearchHit, SearchReport

__all__ = [
    "BaseSearchProvider",
    "CostEstimate",
    "DaveConfig",
    "DaveEngine",
    "DaveExtraction",
    "SearchHit",
    "SearchReport",
    "StreamEvent",
    "extract",
    "extract_sync",
    "recipes",
    "search_extract",
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


async def search_extract(
    query: str,
    schema_or_prompt: type[T] | str | None = None,
    *,
    prompt: str | None = None,
    config: DaveConfig | None = None,
    provider: BaseSearchProvider | str | None = None,
    limit: int = 5,
    **kwargs: Any,
) -> SearchReport:
    """Search the web for ``query`` and extract structured data from each result.

    The library-side counterpart to the ``dave search`` CLI command. The package
    name ``dave.search`` is the provider subpackage, so the callable is named
    ``search_extract`` to avoid shadowing it.
    """
    engine = DaveEngine(config=config)
    return await engine.search(query, schema_or_prompt, prompt=prompt, provider=provider, limit=limit, **kwargs)
