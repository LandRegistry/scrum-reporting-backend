"""empty message

Revision ID: 37572b469aa
Revises: f140c10195
Create Date: 2015-10-18 14:15:08.363529

"""

# revision identifiers, used by Alembic.
revision = '37572b469aa'
down_revision = 'f140c10195'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('daytypes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('daytype_status', sa.String(length=3), nullable=False),
    sa.Column('daytype_name', sa.String(length=100), nullable=False),
    sa.Column('daytype_color', sa.String(length=6), nullable=False),
    sa.Column('daytype_day', sa.Float(), nullable=False),
    sa.Column('daytype_order', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('daytypes')
    ### end Alembic commands ###
