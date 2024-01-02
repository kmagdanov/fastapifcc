"""add content column to posts table

Revision ID: b77fb261693a
Revises: 891bcc587eb9
Create Date: 2024-01-01 21:25:25.660211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b77fb261693a'
down_revision: Union[str, None] = '891bcc587eb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
