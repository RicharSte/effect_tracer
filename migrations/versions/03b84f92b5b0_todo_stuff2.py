"""Todo stuff2

Revision ID: 03b84f92b5b0
Revises: a1a700aebf23
Create Date: 2020-12-31 00:27:19.279717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03b84f92b5b0'
down_revision = 'a1a700aebf23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('Done', sa.Boolean(), nullable=True))
    op.drop_column('todo', 'complete')
    op.drop_column('todo', 'done')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('done', sa.BOOLEAN(), nullable=True))
    op.add_column('todo', sa.Column('complete', sa.BOOLEAN(), nullable=True))
    op.drop_column('todo', 'Done')
    # ### end Alembic commands ###
