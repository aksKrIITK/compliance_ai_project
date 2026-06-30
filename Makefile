.PHONY: dev down test lint migrate seed deploy

# One command — FastAPI + Postgres + Redis + MinIO + frontend
dev:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f api

test:
	pytest tests/ -v --cov=backend --cov-report=term-missing

lint:
	ruff check backend/ tests/
	mypy backend/

migrate:
	cd backend && alembic upgrade head

seed:
	python -m backend.db.seed

deploy:
	gcloud builds submit --config deploy/cloudrun/cloudbuild.yaml
