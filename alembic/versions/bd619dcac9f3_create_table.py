"""create_table

Revision ID: bd619dcac9f3
Revises: 8ccd5e6a671c
Create Date: 2024-01-11 14:50:16.464946

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd619dcac9f3'
down_revision: Union[str, None] = '8ccd5e6a671c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user',
                    sa.Column('id', sa.String, primary_key=True, index=True),
                    sa.Column('name', sa.String),
                    sa.Column('gpa', sa.String),
                    sa.Column('email', sa.String),
                    )

def downgrade() -> None:
    op.drop_table('user')
