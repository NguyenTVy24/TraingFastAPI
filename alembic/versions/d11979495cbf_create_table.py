"""create_table

Revision ID: d11979495cbf
Revises: bd619dcac9f3
Create Date: 2024-01-11 15:10:02.795342

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd11979495cbf'
down_revision: Union[str, None] = 'bd619dcac9f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('projects',
                    sa.Column('id', sa.String, primary_key=True, index=True),
                    sa.Column('description', sa.String),
                    sa.Column('id_user', sa.String, sa.ForeignKey("user.id")),
                    )


def downgrade() -> None:
    op.drop_table('projects')
