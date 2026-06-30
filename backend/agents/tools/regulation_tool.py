"""Structured regulation DB lookup by jurisdiction."""

import json
from pathlib import Path

from backend.config.settings import settings


async def lookup_regulations(jurisdictions: list[str]) -> list[dict]:
    data_path = Path(settings.regulation_data_path)
    results = []
    for json_file in data_path.rglob("*.json"):
        reg = json.loads(json_file.read_text(encoding="utf-8"))
        if reg.get("jurisdiction", "").upper() in [j.upper() for j in jurisdictions]:
            results.append(reg)
    return results
