"""Time and Users added

Revision ID: ea62c4dd1a82
Revises: 03b84f92b5b0
Create Date: 2021-01-03 19:50:09.727660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea62c4dd1a82'
down_revision = '03b84f92b5b0'
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
