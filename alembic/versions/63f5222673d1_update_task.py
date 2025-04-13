"""update-task

Revision ID: 63f5222673d1
Revises: 8037a85bae46
Create Date: 2025-04-13 20:47:54.271874

"""
import sqlmodel
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '63f5222673d1'
down_revision: Union[str, None] = '8037a85bae46'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('parent', sa.Integer(), nullable=True))
    op.add_column('task', sa.Column('base_start', sa.DateTime(), nullable=True))
    op.add_column('task', sa.Column('base_end', sa.DateTime(), nullable=True))
    op.add_column('task', sa.Column('base_duration', sa.Integer(), nullable=True))
    op.alter_column('task', 'start',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('task', 'duration',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('task', 'text',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('task', 'progress',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('task', 'type',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('task', 'open',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('task', 'lazy',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_constraint('task_parent_id_fkey', 'task', type_='foreignkey')
    op.create_foreign_key(None, 'task', 'task', ['parent'], ['id'])
    op.drop_column('task', 'parent_id')
    op.drop_column('task', 'index')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('index', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('task', sa.Column('parent_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.create_foreign_key('task_parent_id_fkey', 'task', 'task', ['parent_id'], ['id'])
    op.alter_column('task', 'lazy',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('task', 'open',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('task', 'type',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('task', 'progress',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('task', 'text',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('task', 'duration',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('task', 'start',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_column('task', 'base_duration')
    op.drop_column('task', 'base_end')
    op.drop_column('task', 'base_start')
    op.drop_column('task', 'parent')
    # ### end Alembic commands ###
