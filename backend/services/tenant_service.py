"""provision schema, enforce plan limits, usage metering."""

PLAN_LIMITS = {"starter": 10, "pro": 100, "enterprise": 10000}


class TenantService:
    async def check_scan_limit(self, tenant_id: str, plan: str = "starter") -> bool:
        # Placeholder — query scan_count from DB in production
        return True

    async def increment_scan_count(self, tenant_id: str) -> int:
        return 1
