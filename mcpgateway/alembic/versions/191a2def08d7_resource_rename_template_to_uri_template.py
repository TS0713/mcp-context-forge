"""resource_rename_template_to_uri_template

Revision ID: 191a2def08d7
Revises: f3a3a3d901b8
Create Date: 2025-11-17 21:20:05.223248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '191a2def08d7'
down_revision: Union[str, Sequence[str], None] = 'f3a3a3d901b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Rename column template → uri_template
    with op.batch_alter_table("resources") as batch_op:
        batch_op.alter_column("template", new_column_name="uri_template")


def downgrade() -> None:
    """Downgrade schema."""
    # Revert column uri_template → template
    with op.batch_alter_table("resources") as batch_op:
        batch_op.alter_column("uri_template", new_column_name="template")