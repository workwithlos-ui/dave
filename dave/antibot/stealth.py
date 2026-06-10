"""Polite anti-detection helpers.

DAVE does not solve CAPTCHAs or bypass access controls. It detects challenges and raises clear errors.
"""

from __future__ import annotations

import random
from dataclasses import dataclass

COMMON_USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
]

CAPTCHA_MARKERS = [
    "captcha",
    "cf-challenge",
    "g-recaptcha",
    "hcaptcha",
    "are you human",
    "bot detection",
    "verify you are human",
]


class UserAgentRotator:
    """Select user agents from a curated pool."""

    def __init__(self, user_agents: list[str] | None = None) -> None:
        self.user_agents = user_agents or COMMON_USER_AGENTS

    def get(self) -> str:
        """Return one user agent."""
        return random.choice(self.user_agents)


@dataclass(slots=True)
class DelayPolicy:
    """Random request delay policy."""

    min_seconds: float = 0.0
    max_seconds: float = 1.5

    def next_delay(self) -> float:
        """Return the next randomized delay."""
        if self.max_seconds < self.min_seconds:
            raise ValueError("max_seconds must be greater than or equal to min_seconds")
        return random.uniform(self.min_seconds, self.max_seconds)


def random_headers(user_agent: str | None = None) -> dict[str, str]:
    """Build browser-like headers."""
    return {
        "User-Agent": user_agent or UserAgentRotator().get(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": random.choice(["en-US,en;q=0.9", "en-GB,en;q=0.8", "en;q=0.7"]),
        "DNT": random.choice(["0", "1"]),
        "Upgrade-Insecure-Requests": "1",
    }


def detect_captcha(html: str) -> bool:
    """Return True when a page appears to contain a CAPTCHA or bot challenge."""
    lower = html.lower()
    return any(marker in lower for marker in CAPTCHA_MARKERS)
