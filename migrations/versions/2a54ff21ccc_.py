"""empty message

Revision ID: 2a54ff21ccc
Revises: None
Create Date: 2015-10-08 14:05:23.764290

"""

# revision identifiers, used by Alembic.
revision = '2a54ff21ccc'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('programmes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('programme_name', sa.String(length=100), nullable=False),
    sa.Column('programme_manager', sa.String(length=100), nullable=True),
    sa.Column('service_manager', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('programme_id', sa.Integer(), nullable=False),
    sa.Column('project_name', sa.String(length=100), nullable=False),
    sa.Column('product_owner', sa.String(length=100), nullable=True),
    sa.Column('scrum_master', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projects')
    op.drop_table('programmes')
    ### end Alembic commands ###
