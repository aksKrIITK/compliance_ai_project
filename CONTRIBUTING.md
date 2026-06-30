# Contributing to Regula Platform

## Adding a new country's regulation set

The moat of this project is `regulation-data/` — a community-maintained, machine-readable compliance corpus.

### 1. Create the JSON file

Add `regulation-data/<region>/<law_name>.json` following this schema:

```json
{
  "id": "india-dpdp-2023",
  "name": "Digital Personal Data Protection Act, 2023",
  "jurisdiction": "IN",
  "category": "privacy",
  "version": "2023-08-11",
  "effective_date": "2024-01-01",
  "summary": "India's primary data protection law.",
  "obligations": [
    {
      "id": "consent",
      "title": "Valid consent required",
      "description": "Data fiduciaries must obtain consent before processing personal data.",
      "severity": "high",
      "articles": ["Section 6"]
    }
  ],
  "penalties": {
    "max_fine_inr": 250000000000,
    "description": "Up to ₹250 crore per violation"
  }
}
```

### 2. Validate locally

```bash
make seed   # Idempotent — loads all JSON into Postgres
make test   # regulation_service tests must pass
```

### 3. Open a PR

Use the **Regulation Request** issue template. Include:

- Source URL (official gazette / regulator site)
- Jurisdiction code (ISO 3166-1 alpha-2)
- Industry tags if applicable (`fintech`, `healthtech`, etc.)

### Code standards

- `ruff` + `mypy` must pass (`make lint`)
- Coverage must stay above 80% (`make test`)
- Use `MockLLM` in tests — never call paid APIs in CI
