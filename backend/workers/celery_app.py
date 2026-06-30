"""Redis broker, beat schedule: daily sync + weekly rescan."""

from celery import Celery
from celery.schedules import crontab

from backend.config.settings import settings

celery_app = Celery("regula", broker=settings.celery_broker_url)
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    beat_schedule={
        "regulation-sync-daily": {
            "task": "backend.workers.tasks.regulation_sync.sync_regulations",
            "schedule": crontab(hour=2, minute=0),
        },
        "weekly-rescan": {
            "task": "backend.workers.tasks.scan_task.rescan_all_tenants",
            "schedule": crontab(day_of_week=0, hour=3),
        },
    },
)
celery_app.autodiscover_tasks(["backend.workers.tasks"])
