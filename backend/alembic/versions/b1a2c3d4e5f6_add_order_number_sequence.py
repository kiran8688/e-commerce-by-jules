"""add order number sequence

Revision ID: b1a2c3d4e5f6
Revises: ac831b562b49
Create Date: 2026-05-20 10:00:00.000000

"""
from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'b1a2c3d4e5f6'
down_revision: str | None = 'ac831b562b49'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.execute("CREATE SEQUENCE order_number_seq START WITH 1")


def downgrade() -> None:
    op.execute("DROP SEQUENCE order_number_seq")
