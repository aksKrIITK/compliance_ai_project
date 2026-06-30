"""jurisdiction detection, regulation matching, sync."""

import json
from pathlib import Path
from typing import Any

from backend.config.settings import settings


class RegulationService:
    def __init__(self):
        self.data_path = Path(settings.regulation_data_path)

    async def list_regulations(
        self, country: str | None = None, industry: str | None = None
    ) -> dict[str, Any]:
        regulations = []
        for json_file in self.data_path.rglob("*.json"):
            data = json.loads(json_file.read_text(encoding="utf-8"))
            if country and data.get("jurisdiction", "").upper() != country.upper():
                continue
            regulations.append(
                {
                    "id": data["id"],
                    "name": data["name"],
                    "jurisdiction": data.get("jurisdiction"),
                    "category": data.get("category"),
                    "version": data.get("version"),
                }
            )
        return {"regulations": regulations, "count": len(regulations)}

    async def get_by_jurisdiction(self, jurisdiction: str) -> list[dict]:
        result = await self.list_regulations(country=jurisdiction)
        return result["regulations"]
