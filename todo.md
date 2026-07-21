# Automation project — session TODO list

Work through these **one item per session**. Mark each as done when finished (`[x]`).

Items below match the agreed plan: libs + tree are already scaffolded; everything else is still open.

---

## Decisions (can be its own session)

- [ ] **1. Pick concrete demo target(s)**
  - Choose a real UI site and a real/mock REST API to exercise against
  - Candidates discussed: UI — `the-internet.herokuapp.com` or `practicetestautomation.com`; API — `reqres.in` or `jsonplaceholder.typicode.com`
  - Until this is done, config values and page/client names stay generic

---

## Core engine (`src/automation/core/`)

- [ ] **2. Config layer**
  - Implement `Settings` with pydantic-settings
  - Per-environment files under `core/config/environments/` (`dev.yaml`, `staging.yaml`, `ci.yaml`)
  - `get_settings()` accessor + wire into root `tests/conftest.py`
  - Align `.env.example` keys with the real Settings model

- [ ] **3. Logging**
  - Implement `configure_logging()` in `core/log_config.py` (stdlib `dictConfig`)
  - Write logs under `artifacts/logs/`
  - Call from shared fixtures so every test run is logged consistently

- [ ] **4. Exception hierarchy**
  - Add shallow custom exceptions in `core/exceptions/`: `AutomationError`, `ConfigError`, `UiError`, `ApiClientError`
  - Use them from the HTTP client and UI helpers instead of leaking raw library exceptions

- [ ] **5. HTTP client (`core/api/`)**
  - Implement concrete `HttpClient` on top of httpx
  - Base URL, headers, timeouts, request/response logging, retries via tenacity
  - Raise `ApiClientError` on failures

- [ ] **6. UI base helpers (`core/ui/`)**
  - Implement thin `BasePage` (and optional `BaseComponent`) wrapping Playwright
  - Common actions only (`goto`, `click`, `fill`, …) — no app-specific locators

- [ ] **7. Mock server helpers (`core/mock_server/`)**
  - Wrap pytest-httpserver lifecycle / stub registration
  - Keep stub *payloads* in `tests/data/mock_api/` (data-driven)

- [ ] **8. Reporting helpers (`core/reporting/`)**
  - Allure step / attach helpers (`step()`, screenshot/log attachment)
  - Screenshot-on-failure (and optionally attach traces/videos) hooked from UI `conftest.py`

---

## App / business layer (`src/automation/app/`)

> Best done **after** demo targets (#1) are chosen.

- [ ] **9. Domain models (`app/models/`)**
  - Pydantic (or dataclass) domain entities shared across UI + API + workflows

- [ ] **10. API DTOs (`app/api/models/`)**
  - Wire-format `*Request` / `*Response` pydantic models for the chosen API

- [ ] **11. API clients (`app/api/clients/`)**
  - Product-specific clients built on `HttpClient` (verb methods: `create`, `get`, `list`, …)

- [ ] **12. UI pages (`app/ui/pages/`)**
  - Page objects for the chosen demo site (locators + actions only; no assertions)

- [ ] **13. UI components (`app/ui/components/`)**
  - Shared widgets (nav, dialogs, etc.) if the demo UI needs them

- [ ] **14. Workflows (`app/workflows/`)**
  - Multi-step flows as **functions** by default (`login()`, …); class only if stateful

- [ ] **15. Domain assertions (`app/assertions/`)**
  - `assert_*` helper functions for business-level checks used by tests

---

## Tests

- [ ] **16. Shared / layer fixtures**
  - Flesh out `tests/conftest.py`, `tests/ui/conftest.py`, `tests/api/conftest.py`
  - Inject Settings, pages, clients; keep tests thin

- [ ] **17. First API tests + mock data**
  - Real and/or mocked API tests under `tests/api/`
  - Static payloads under `tests/data/api/` and `tests/data/mock_api/`

- [ ] **18. First UI tests + UI data**
  - Smoke UI tests under `tests/ui/`
  - Static data under `tests/data/ui/` / `tests/data/shared/`

---

## Quality, parallel, CI, reporting polish

- [ ] **19. Pre-commit + quality tooling**
  - `.pre-commit-config.yaml` running ruff (+ optionally pyright)
  - Confirm `uv run ruff check` / `uv run pyright` work on the package

- [ ] **20. Parallelism & markers**
  - Tune pytest-xdist (`-n auto`, grouping if needed)
  - Use markers (`smoke`, `regression`, `ui`, `api`) consistently in tests and docs

- [ ] **21. Allure / HTML reporting end-to-end**
  - Default `--alluredir=artifacts/allure-results`
  - Document local `allure serve` / generate flow
  - Optional pytest-html fallback into `artifacts/`

- [ ] **22. Jenkins / CI pipeline**
  - Add `Jenkinsfile`: `uv sync --frozen`, Playwright browser install, pytest, publish Allure
  - Document required agent tools (uv, Allure CLI, browsers)

---

## How to use this list

1. Pick the next unchecked item.
2. Open a new Cursor session focused on that item only.
3. Implement / decide, then mark it `[x]` here before stopping.
