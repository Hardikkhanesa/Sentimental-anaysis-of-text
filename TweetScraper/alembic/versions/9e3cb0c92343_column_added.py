"""column added

Revision ID: 9e3cb0c92343
Revises: 8db337e39f5d
Create Date: 2019-09-30 19:26:02.532138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e3cb0c92343'
down_revision = '8db337e39f5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tweetmeta', sa.Column('extra', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tweetmeta', 'extra')
    # ### end Alembic commands ###