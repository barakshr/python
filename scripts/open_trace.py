#!/usr/bin/env python3
"""Open a Playwright trace.zip in the Trace Viewer (browser).

Usage:
  uv run python scripts/open_trace.py
  uv run python scripts/open_trace.py path/to/trace.zip
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "test-results"


def latest_trace() -> Path:
    traces = sorted(RESULTS.rglob("trace.zip"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not traces:
        raise SystemExit(f"No trace.zip found under {RESULTS}")
    return traces[0]


def main() -> None:
    if len(sys.argv) > 1:
        trace = Path(sys.argv[1]).expanduser().resolve()
        if not trace.is_file():
            raise SystemExit(f"File not found: {trace}")
    else:
        trace = latest_trace()

    print(f"Opening {trace}")
    subprocess.run(["playwright", "show-trace", str(trace)], check=True)


if __name__ == "__main__":
    main()
