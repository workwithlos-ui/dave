<p align="center">
  <h1 align="center">DAVE</h1>
</p>

<p align="center">
  <strong>AI-powered scraping without LangChain, graph DSLs, or dependency bloat.</strong>
</p>

<p align="center">
  Give DAVE a URL and get clean, validated, structured data. DAVE ships with five runtime dependencies, no LangChain dependency, and no graph framework to learn. Use a prompt, a Pydantic schema, a built-in recipe, or nothing at all.
</p>

<p align="center">
  <a href="https://github.com/workwithlos-ui/dave/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/workwithlos-ui/dave/ci.yml?branch=main&label=tests" alt="Tests"></a>
  <a href="https://pypi.org/project/dave-ai/"><img src="https://img.shields.io/pypi/v/dave-ai?label=pypi" alt="PyPI"></a>
  <a href="https://pypi.org/project/dave-ai/"><img src="https://img.shields.io/pypi/pyversions/dave-ai" alt="Python versions"></a>
  <a href="https://pypi.org/project/dave-ai/"><img src="https://img.shields.io/pypi/dm/dave-ai?label=downloads" alt="Downloads"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/workwithlos-ui/dave" alt="License"></a>
</p>

---

## Try it in 10 seconds

```bash
pip install dave-ai
dave extract "https://openai.com" --recipe company_info
```

Or use the library in one line:

```python
import dave

result = await dave.extract("https://competitor.com")
```

That call has no prompt and no schema. DAVE still returns intelligent structured data by detecting the page type, important entities, key facts, calls to action, prices, contact signals, and links. This is the zero-config path for demos, exploration, and first-pass research.

## The 3-line version

```python
import dave

result = await dave.extract("https://example.com", "get the title and description")
print(result)
```

DAVE is designed for developers who need more than a prototype but do not want a full LangChain dependency tree. It combines fetcher selection, LLM extraction, Pydantic validation, caching, retries, rate limits, heuristic confidence scoring, cost tracking, batch jobs, and a plugin system in one typed Python package with only five runtime dependencies.

## Why DAVE?

Most AI scraping tools are impressive in a notebook and heavy in a production job. ScrapeGraphAI publicly documents a graph-based API and a broad LangChain dependency stack. DAVE takes the opposite path: a small typed core, direct fetcher and extractor interfaces, and production controls that are easy to reason about.

| What developers need | How DAVE handles it |
| --- | --- |
| Keep dependency risk low | Ships with five runtime dependencies: Beautiful Soup, HTTPX, Pydantic, Rich, and Typer |
| Avoid framework lock-in | Uses no LangChain dependency and no graph DSL |
| Scrape static and JavaScript-heavy pages | Auto-selects HTTP or Playwright, with extension points for Firecrawl and Crawl4AI |
| Extract with a prompt or a schema | Accepts natural language prompts, Pydantic models, built-in recipes, or no prompt at all |
| Trust the output | Validates schema extraction through Pydantic and reports transparent heuristic confidence |
| Keep costs visible | Estimates tokens before runs and tracks cost after runs |
| Run hundreds of URLs | Includes batch mode, retries, rate limits, progress, and JSON output |
| Avoid building glue code | Ships caching, queueing, structured logging, CLI commands, and plugin registration |

Confidence is a transparent heuristic based on evidence presence and source-text overlap, not a model-reported probability.

## Feature comparison

This table is intentionally conservative. It compares publicly documented positioning and core APIs, not private roadmaps or unmeasured performance claims.

| Capability | DAVE | ScrapeGraphAI | Firecrawl | Crawl4AI | BeautifulSoup |
| --- | --- | --- | --- | --- | --- |
| Core positioning | Lean Python extraction engine | Graph-based AI scraping library | Hosted web data API | Open LLM-friendly crawler and scraper | HTML and XML parser |
| LangChain dependency in core install | No | Yes, documented in package metadata | Not applicable to hosted API usage | No claim in docs reviewed | No |
| Runtime dependency count in Python package | Five core dependencies | Broad dependency tree in package metadata | SDK plus hosted service | Framework package with browser-focused stack | Parser library |
| Natural-language extraction | Yes | Yes, via graph APIs | Yes, via Extract API | Yes, via LLM extraction strategies | No |
| Schema-shaped extraction | Yes, Pydantic-first | Yes, documented schema examples | Yes, JSON schema in Extract API | Yes, CSS, XPath, and LLM strategies | Manual code |
| Zero-prompt, zero-schema URL extraction | Yes, built into DAVE | Not documented in sources reviewed | Prompt or schema documented for Extract | Not documented in sources reviewed | Manual code |
| Built-in recipes for common pages | Yes, company, pricing, jobs, contact, product, reviews | Not a primary documented abstraction | Not a primary documented abstraction | Not a primary documented abstraction | Manual code |
| Fetching model | HTTP plus optional Playwright, plugin fetchers | Playwright and provider integrations documented | Hosted scrape, crawl, search, extract, interact API | Browser crawler with advanced controls | Bring your own HTTP client |
| Search plus extraction | Planned fast-follow | SearchGraph documented | Search and Extract documented | Adaptive crawling documented | Manual code |
| Best fit | Lean structured extraction with production controls | Graph-oriented AI scraping workflows | Managed crawling and extraction API | Configurable open crawler framework | Deterministic HTML parsing |

Sources reviewed: [ScrapeGraphAI README](https://github.com/ScrapeGraphAI/Scrapegraph-ai), [ScrapeGraphAI package metadata](https://github.com/ScrapeGraphAI/Scrapegraph-ai/blob/main/pyproject.toml), [Firecrawl docs](https://docs.firecrawl.dev/introduction), [Firecrawl Extract docs](https://docs.firecrawl.dev/features/extract), [Crawl4AI docs](https://docs.crawl4ai.com/), and [Beautiful Soup docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

## Zero-config magic

DAVE can run with no prompt and no schema:

```python
import dave

page = await dave.extract("https://stripe.com")
```

A typical result looks like this:

```json
{
  "page_type": "company_or_content",
  "title": "Stripe",
  "summary": "Financial infrastructure for the internet",
  "key_entities": ["Stripe", "Payments", "Billing"],
  "key_facts": ["Stripe builds programmable financial services for businesses."],
  "links": ["https://stripe.com/pricing"],
  "contacts": {"emails": [], "phones": []},
  "prices": [],
  "products": ["Payments", "Billing", "Connect"],
  "jobs": [],
  "calls_to_action": ["Start now", "Contact sales"]
}
```

Zero-config extraction is not a replacement for schemas in critical workflows. It is the fastest way to inspect a new page, build lead lists, prototype competitive intelligence, and discover what schema you should use next.

## Recipes that work out of the box

DAVE recipes are typed extraction flows for the web pages developers scrape every week.

| Recipe | Python | CLI |
| --- | --- | --- |
| Company info | `await dave.recipes.company_info(url)` | `dave extract URL --recipe company_info` |
| Pricing tiers | `await dave.recipes.pricing(url)` | `dave extract URL --recipe pricing` |
| Job listings | `await dave.recipes.job_listings(url)` | `dave extract URL --recipe job_listings` |
| Contact info | `await dave.recipes.contact_info(url)` | `dave extract URL --recipe contact_info` |
| Product features | `await dave.recipes.product_features(url)` | `dave extract URL --recipe product_features` |
| Reviews and testimonials | `await dave.recipes.reviews(url)` | `dave extract URL --recipe reviews` |

Example:

```python
import dave

company = await dave.recipes.company_info("https://linear.app")
pricing = await dave.recipes.pricing("https://linear.app/pricing")
```

The returned objects are Pydantic models, so they are easy to validate, serialize, and pass into downstream systems.

## Beautiful CLI output

DAVE is built to look good in the terminal because the terminal is where scraping jobs fail, recover, and prove they are working.

```text
$ dave extract "https://openai.com" --recipe company_info

╭──────────── Cost estimate ────────────╮
│ This extraction will use about        │
│ 2,000 tokens for roughly $0.003000.   │
╰───────────────────────────────────────╯
Proceed? [Y/n] y

╭──── Data Acquisition and Validation Engine ────╮
│ DAVE is extracting structured data              │
╰────────────────────────────────────────────────╯
+ Fetching page with auto fetcher 0:00:01
field name = OpenAI
field description = AI research and deployment company
field tech_stack = ["Python", "Kubernetes", "LLM APIs"]
field social_links = ["https://twitter.com/openai"]

╭────────────────── DAVE Extraction: company_info ──────────────────╮
│ Field        │ Value                                               │
│ name         │ OpenAI                                              │
│ description  │ AI research and deployment company                  │
│ founders     │ []                                                  │
│ funding      │ null                                                │
│ employees    │ null                                                │
│ tech_stack   │ ["Python", "Kubernetes", "LLM APIs"]              │
╰───────────────────────────────────────────────────────────────────╯

Run Metadata
confidence  0.91
cost_usd    0.003
fetcher     playwright
final_url   https://openai.com
```

Use machine-readable output when you need it:

```bash
dave extract "https://example.com" --prompt "get the title" --output json
```

## Batch mode

Process hundreds of URLs with progress, retries, cache hits, and a cost summary.

```bash
dave batch urls.txt --recipe pricing --output results.json
```

The input file is plain text:

```text
https://example.com/pricing
https://another-example.com/pricing
https://vendor.example/pricing
```

DAVE writes a JSON array with one item per URL. Failed URLs include the error message and successful URLs include data, confidence, evidence, cost, final URL, and fetcher metadata.

## Cost calculator

DAVE estimates token usage before running an extraction.

```text
This extraction will use about 2,000 tokens for roughly $0.003000.
Proceed? [Y/n]
```

The estimate uses the selected model, prompt, schema, and fetched page text. After extraction, DAVE returns tracked usage and cost metadata so teams can monitor spending by job, domain, recipe, or customer.

## Streaming extraction

When `--stream` is enabled, DAVE emits field events as data is found instead of waiting until the full extraction is complete.

```python
from dave.core.engine import DaveEngine

engine = DaveEngine()

async for event in engine.stream_extract("https://example.com", "get title and pricing"):
    print(event.type, event.message, event.data)
```

Streaming is useful for long pages, operator dashboards, live demos, and batch jobs where early partial output is better than silence.

## Pydantic-first extraction

```python
from pydantic import BaseModel, Field
import dave

class PricingTier(BaseModel):
    name: str
    price: str | None = None
    features: list[str] = Field(default_factory=list)

class PricingPage(BaseModel):
    tiers: list[PricingTier] = Field(default_factory=list)

pricing = await dave.extract("https://vendor.example/pricing", PricingPage)
print(pricing.model_dump())
```

Every schema extraction is validated before it is returned. If a provider returns invalid JSON or mismatched data, DAVE fails loudly instead of silently contaminating your pipeline.

## Architecture

```mermaid
flowchart LR
    A[URL plus prompt, schema, recipe, or zero-config] --> B[DAVE Engine]
    B --> C{Fetcher Router}
    C --> D[HTTP Fetcher]
    C --> E[Playwright Fetcher]
    C --> F[Firecrawl or Crawl4AI Plugin]
    D --> G[Cache and Rate Limiter]
    E --> G
    F --> G
    G --> H[Chunker]
    H --> I{LLM Provider}
    I --> J[OpenAI]
    I --> K[Anthropic]
    I --> L[Ollama]
    H --> M[Pydantic Validator]
    J --> M
    K --> M
    L --> M
    M --> N[Confidence Scoring]
    N --> O[Structured Data]
    O --> P[CLI, Python API, Batch Jobs]
```

## Fetchers

DAVE ships with a multi-fetcher backend and a simple routing model.

| Fetcher | Use it for | Command |
| --- | --- | --- |
| `auto` | Let DAVE choose based on page signals | `--fetcher auto` |
| `http` | Fast static pages and APIs | `--fetcher http` |
| `playwright` | JavaScript-rendered pages | `--fetcher playwright` |
| plugin | Firecrawl, Crawl4AI, internal crawlers, or custom fetchers | `--fetcher your_name` |

Proxy rotation is configured through `DaveConfig.proxies`. Bring your own proxy URLs and DAVE will rotate them across requests.

## Plugin system

DAVE is designed for community extensions. Register custom fetchers and extractors without forking the project.

```python
from dave.plugins import register_fetcher
from dave.fetchers.base import Fetcher, FetchResult

class InternalFetcher(Fetcher):
    name = "internal"

    async def fetch(self, url: str) -> FetchResult:
        return FetchResult(
            url=url,
            final_url=url,
            status_code=200,
            content="<html><title>Internal</title></html>",
            content_type="text/html",
            elapsed_ms=12.0,
            rendered=False,
        )

register_fetcher("internal", InternalFetcher)
```

```bash
dave extract "https://internal.example" --fetcher internal --prompt "summarize this page"
```

Plugins make it possible to add authenticated browser sessions, enterprise crawlers, proxy vendors, custom LLM routers, domain-specific validators, and private data enrichment steps.

## Benchmarks coming

A reproducible benchmark suite is in development. We will publish real numbers, not targets, once it lands. Track it in issue #1.

The benchmark suite will measure end-to-end extraction from real product, pricing, jobs, documentation, and contact pages. It will publish fixtures, scripts, provider settings, hardware assumptions, network assumptions, and raw results so maintainers and users can reproduce the numbers.

## Configuration

```python
from dave.core.config import DaveConfig, LLMConfig

config = DaveConfig(
    fetcher="auto",
    llm=LLMConfig(provider="openai", model="gpt-4o-mini"),
    cache_path=".dave/cache.sqlite3",
    rate_limit_per_domain=2.0,
    proxies=["http://user:pass@proxy.example:8080"],
)
```

Environment variables are supported for common provider keys:

| Variable | Purpose |
| --- | --- |
| `DAVE_LLM_PROVIDER` | Select `openai`, `anthropic`, `ollama`, or `mock` |
| `DAVE_LLM_API_KEY` | Provider API key |
| `OPENAI_API_KEY` | OpenAI fallback key |
| `ANTHROPIC_API_KEY` | Anthropic fallback key |
| `DAVE_LLM_MODEL` | Model override |

## Local development

```bash
git clone https://github.com/workwithlos-ui/dave.git
cd dave
python -m pip install -e ".[dev]"
pytest
ruff check .
```

Install Playwright support when you want JavaScript rendering:

```bash
python -m pip install -e ".[playwright]"
python -m playwright install chromium
```

## Project structure

```text
dave/
  core/          Engine, config, retries, queue, rate limits
  fetchers/      HTTP, Playwright, Firecrawl, Crawl4AI, router
  extractors/    LLM extraction, schema validation, confidence
  antibot/       Proxy and user-agent helpers
  cache/         SQLite response cache
  monitoring/    Cost tracking and structured logging
  cli/           Rich and Typer command line interface
  plugins.py     Community extension registry
  recipes.py     Built-in extraction recipes
```

## Roadmap

| Milestone | Status |
| --- | --- |
| Zero-config extraction | Done |
| Built-in recipes | Done |
| Streaming CLI output | Done |
| Batch mode | Done |
| Plugin registry | Done |
| Hosted benchmark dashboard | Planned |
| More recipe packs | Planned |
| OpenTelemetry traces | Planned |

## Contributing

DAVE is built for developers who scrape in production. Contributions should improve reliability, ergonomics, tests, documentation, or real-world extraction quality.

Before opening a pull request, please run:

```bash
pytest
ruff check .
python -m compileall dave
```

Good first contributions include new recipes, fetcher plugins, provider adapters, benchmark cases, docs examples, and domain-specific validators. Please keep code typed, keep tests meaningful, and do not add em dash characters to any file.

## License

DAVE is released under the MIT License. See [LICENSE](LICENSE).
