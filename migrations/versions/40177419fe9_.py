"""empty message

Revision ID: 40177419fe9
Revises: 24f73580841
Create Date: 2015-10-21 20:24:30.015128

"""

# revision identifiers, used by Alembic.
revision = '40177419fe9'
down_revision = '24f73580841'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sprints', sa.Column('burndown_total', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sprints', 'burndown_total')
    ### end Alembic commands ###