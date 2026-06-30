"""email (SendGrid), Slack, signed webhooks, in-app."""

from backend.api.v1.webhooks import sign_webhook_payload


class NotificationService:
    async def send_email(self, to: str, subject: str, body: str) -> None:
        _ = (to, subject, body)

    async def send_webhook(self, url: str, payload: bytes) -> dict:
        signature = sign_webhook_payload(payload)
        return {"url": url, "signature": signature, "status": "sent"}

    async def notify_scan_complete(self, tenant_id: str, scan_id: str, score: float) -> None:
        _ = (tenant_id, scan_id, score)
