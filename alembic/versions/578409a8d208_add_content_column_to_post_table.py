"""add content column to post table

Revision ID: 578409a8d208
Revises: bb77361e6822
Create Date: 2024-09-14 14:58:41.094995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '578409a8d208'
down_revision: Union[str, None] = 'bb77361e6822'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", 'content')
    pass
