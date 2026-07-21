# automation

Python UI + API test automation framework (Playwright + httpx + pytest).

## Setup

```bash
# Requires uv (https://docs.astral.sh/uv/)
uv sync
uv run playwright install chromium
```

## Run tests

```bash
uv run pytest
uv run pytest -m smoke
uv run pytest -n auto
uv run pytest --alluredir=artifacts/allure-results
```

## Project layout

- `src/automation/core/` — reusable, app-agnostic engine
- `src/automation/app/` — product-specific pages, clients, workflows, models
- `tests/` — thin UI/API tests + data
- `artifacts/` — generated logs, screenshots, traces, Allure output (gitignored)

See `todo.md` for the remaining design/implementation checklist (one item per session).
