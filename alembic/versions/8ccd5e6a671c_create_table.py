"""create_table

Revision ID: 8ccd5e6a671c
Revises: 
Create Date: 2024-01-11 11:13:51.209917

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ccd5e6a671c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('textapi',
                    sa.Column('id_cou', sa.String, primary_key=True, index=True),
                    sa.Column('title', sa.String),
                    )


def downgrade() -> None:
    op.drop_table('textapi')
