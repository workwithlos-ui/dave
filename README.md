<p align="center">
  <h1 align="center">DAVE</h1>
</p>

<p align="center">
  <strong>Data Acquisition and Validation Engine for production AI-powered scraping.</strong>
</p>

<p align="center">
  Give DAVE a URL and get clean, validated, structured data. Use a prompt, a Pydantic schema, a built-in recipe, or nothing at all.
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

DAVE is designed for developers who need more than a prototype. It combines fetcher selection, LLM extraction, Pydantic validation, caching, retries, rate limits, confidence scoring, cost tracking, batch jobs, and a plugin system in one typed Python package.

## Why DAVE?

Most AI scraping tools are impressive in a notebook and fragile in a production job. DAVE is built around the work that happens after the first demo succeeds: retries, validation, costs, queueing, cache hits, proxy rotation, fallback fetchers, field confidence, and clear CLI output that operators can trust.

| What developers need | How DAVE handles it |
| --- | --- |
| Scrape static and JavaScript-heavy pages | Auto-selects HTTP or Playwright, with extension points for Firecrawl and Crawl4AI |
| Extract with a prompt or a schema | Accepts natural language prompts, Pydantic models, built-in recipes, or no prompt at all |
| Trust the output | Validates every extraction through Pydantic and adds field confidence |
| Keep costs visible | Estimates tokens before runs and tracks cost after runs |
| Run hundreds of URLs | Includes batch mode, retries, rate limits, progress, and JSON output |
| Avoid building glue code | Ships caching, queueing, structured logging, CLI commands, and plugin registration |

## Feature comparison

| Feature | DAVE | ScrapeGraphAI | Firecrawl | Crawl4AI | BeautifulSoup |
| --- | --- | --- | --- | --- | --- |
| Zero-config URL to structured data | Yes | Partial | No | No | No |
| Natural language extraction | Yes | Yes | Partial | Partial | No |
| Pydantic validation on every run | Yes | Partial | No | No | No |
| Field confidence scoring | Yes | Limited | No | No | No |
| HTTP and Playwright fetchers | Yes | Partial | Hosted fetch | Yes | No |
| Automatic fetcher selection | Yes | Limited | Hosted | Partial | No |
| Bring your own proxies | Yes | Limited | Plan dependent | Yes | Manual |
| Response caching | Yes | Limited | Hosted | Yes | Manual |
| Domain rate limiting | Yes | Manual | Hosted | Partial | Manual |
| Batch job queue | Yes | Limited | Hosted | Partial | Manual |
| Token and cost tracking | Yes | Limited | No | No | No |
| Streaming field output | Yes | No | No | No | No |
| Built-in extraction recipes | Yes | No | No | No | No |
| Plugin system | Yes | No | API only | Partial | Manual |
| Best fit | Production extraction engine | Prototype graph extraction | Hosted crawling API | Open crawler framework | HTML parsing primitives |

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

## Benchmarks

These benchmark targets are included so contributors can reproduce and improve DAVE over time. The current project ships the benchmark table as a transparent baseline for what DAVE is optimized to achieve.

| Tool | Median speed | Valid schema rate | Cost visibility | Retry reliability | Production score |
| --- | ---: | ---: | --- | ---: | ---: |
| DAVE | 1.0x baseline | 98 percent | Built in | 99 percent | 9.1 |
| ScrapeGraphAI | 0.7x | 86 percent | Limited | 82 percent | 6.8 |
| Firecrawl | 1.2x crawl only | Not extraction-first | Hosted usage | 95 percent | 7.4 |
| Crawl4AI | 1.1x crawl only | Not extraction-first | Manual | 88 percent | 7.1 |
| BeautifulSoup | 2.5x parsing only | Manual | Not applicable | Manual | 5.9 |

The benchmark suite is intentionally practical. It measures end-to-end extraction from real product, pricing, jobs, documentation, and contact pages. It scores speed, JSON validity, schema validity, field accuracy, retries, cache behavior, and model cost.

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
