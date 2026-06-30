"""Initial schema — tenants, users, documents, regulations, compliance_issues, document_chunks."""

from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector

revision = "001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")
    # Tables created via autogenerate in production — placeholder revision
    pass


def downgrade() -> None:
    pass
