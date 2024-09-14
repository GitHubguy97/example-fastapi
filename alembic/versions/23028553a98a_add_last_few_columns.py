"""Add last few columns

Revision ID: 23028553a98a
Revises: ba1879485654
Create Date: 2024-09-14 16:04:37.797257

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '23028553a98a'
down_revision: Union[str, None] = 'ba1879485654'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('published', sa.Boolean(), nullable = False,
                            server_default = 'TRUE')
                    )
    op.add_column('posts',
                  sa.Column('created_at' , sa.TIMESTAMP(timezone=True),
                            nullable=False, server_default = sa.text('now()'))
                  )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
