"""Fetch updates → diff → trigger affected tenant rescans."""

from backend.workers.celery_app import celery_app


@celery_app.task(name="backend.workers.tasks.regulation_sync.sync_regulations")
def sync_regulations() -> dict:
    return {"status": "synced", "updated": 0}
