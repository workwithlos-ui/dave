from __future__ import annotations

from dave.antibot.proxies import ProxyPool
from dave.antibot.stealth import DelayPolicy, UserAgentRotator, detect_captcha, random_headers


def test_detect_captcha_markers():
    assert detect_captcha("<div>Verify you are human</div>") is True
    assert detect_captcha("<main>Welcome</main>") is False


def test_proxy_pool_removes_failing_proxy():
    pool = ProxyPool(["http://proxy-one", "http://proxy-two"], max_failures=2)
    proxy = pool.next()
    pool.mark_failure(proxy)
    pool.mark_failure(proxy)

    assert proxy not in {pool.next(), pool.next()}


def test_delay_policy_range():
    delay = DelayPolicy(0.1, 0.2).next_delay()
    assert 0.1 <= delay <= 0.2


def test_random_headers_contains_user_agent():
    headers = random_headers(UserAgentRotator(["UA"]).get())
    assert headers["User-Agent"] == "UA"
