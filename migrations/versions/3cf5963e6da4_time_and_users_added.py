"""Time and Users added

Revision ID: 3cf5963e6da4
Revises: ea62c4dd1a82
Create Date: 2021-01-03 19:59:05.370875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cf5963e6da4'
down_revision = 'ea62c4dd1a82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('Done', sa.Boolean(), nullable=True))
    op.add_column('todo', sa.Column('created', sa.DateTime(), nullable=False))
    op.add_column('todo', sa.Column('user_id', sa.Integer(), nullable=True))
    op.alter_column('todo', 'text',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
    op.create_index(op.f('ix_todo_user_id'), 'todo', ['user_id'], unique=False)
    op.create_foreign_key(None, 'todo', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('todo', 'done')
    op.drop_column('todo', 'complete')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('complete', sa.BOOLEAN(), nullable=True))
    op.add_column('todo', sa.Column('done', sa.BOOLEAN(), nullable=True))
    op.drop_constraint(None, 'todo', type_='foreignkey')
    op.drop_index(op.f('ix_todo_user_id'), table_name='todo')
    op.alter_column('todo', 'text',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
    op.drop_column('todo', 'user_id')
    op.drop_column('todo', 'created')
    op.drop_column('todo', 'Done')
    # ### end Alembic commands ###