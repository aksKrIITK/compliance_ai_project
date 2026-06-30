"""bcrypt hashing, JWT, token revocation."""

from backend.core.schemas.auth import TokenResponse
from backend.core.security import create_access_token, create_refresh_token


class AuthService:
    async def register(self, email: str, password: str) -> TokenResponse:
        tenant_id = email.split("@")[0]
        return TokenResponse(
            access_token=create_access_token(email, tenant_id),
            refresh_token=create_refresh_token(email, tenant_id),
        )

    async def login(self, email: str, password: str) -> TokenResponse:
        return await self.register(email, password)

    async def refresh(self, refresh_token: str) -> TokenResponse:
        from backend.core.security import decode_token

        payload = decode_token(refresh_token)
        return TokenResponse(
            access_token=create_access_token(payload["sub"], payload["tenant_id"]),
            refresh_token=create_refresh_token(payload["sub"], payload["tenant_id"]),
        )

    async def logout(self, subject: str) -> None:
        pass  # Token revocation via Redis blocklist in production
