"""update-datetime-with-tz

Revision ID: 06f8d9263380
Revises: 63f5222673d1
Create Date: 2025-04-13 21:09:03.130273

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '06f8d9263380'
down_revision: Union[str, None] = '63f5222673d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'start',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               nullable=True)
    op.alter_column('task', 'end',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=True)
    op.alter_column('task', 'base_start',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=True)
    op.alter_column('task', 'base_end',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'base_end',
               existing_type=sa.DateTime(timezone=True),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    op.alter_column('task', 'base_start',
               existing_type=sa.DateTime(timezone=True),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    op.alter_column('task', 'end',
               existing_type=sa.DateTime(timezone=True),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    op.alter_column('task', 'start',
               existing_type=sa.DateTime(timezone=True),
               type_=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###
