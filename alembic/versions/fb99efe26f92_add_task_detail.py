"""add-task-detail

Revision ID: fb99efe26f92
Revises: 06f8d9263380
Create Date: 2025-04-14 13:13:36.222939

"""
import sqlmodel
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb99efe26f92'
down_revision: Union[str, None] = '06f8d9263380'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('details', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'details')
    # ### end Alembic commands ###
