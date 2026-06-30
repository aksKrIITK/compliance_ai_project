"""run_compliance_scan.delay() — full LangGraph pipeline."""

from backend.workers.celery_app import celery_app


@celery_app.task(name="backend.workers.tasks.scan_task.run_compliance_scan")
def run_compliance_scan(tenant_id: str, document_ids: list[str], jurisdictions: list[str]) -> dict:
    import asyncio
    from backend.services.compliance_service import ComplianceService

    service = ComplianceService()
    result = asyncio.run(service.run_scan(tenant_id, document_ids, jurisdictions))
    return result.model_dump()


@celery_app.task(name="backend.workers.tasks.scan_task.rescan_all_tenants")
def rescan_all_tenants() -> dict:
    return {"status": "scheduled", "tenants": 0}
