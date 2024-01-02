"""add last few columns to posts table

Revision ID: ec5f0bf815d5
Revises: dda1697cd511
Create Date: 2024-01-01 23:35:07.090071

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec5f0bf815d5'
down_revision: Union[str, None] = 'dda1697cd511'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean, nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))


def downgrade() -> None: 
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
