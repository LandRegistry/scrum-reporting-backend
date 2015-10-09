"""empty message

Revision ID: 15d38f6b066
Revises: 2a54ff21ccc
Create Date: 2015-10-09 20:31:49.713186

"""

# revision identifiers, used by Alembic.
revision = '15d38f6b066'
down_revision = '2a54ff21ccc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sprints',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.String(length=100), nullable=False),
    sa.Column('end_date', sa.String(length=100), nullable=True),
    sa.Column('sprint_number', sa.String(length=100), nullable=True),
    sa.Column('sprint_rag', sa.String(length=1), nullable=False),
    sa.Column('sprint_goal', sa.String(length=500), nullable=True),
    sa.Column('sprint_deliverables', sa.String(length=500), nullable=True),
    sa.Column('sprint_challenges', sa.String(length=500), nullable=False),
    sa.Column('agreed_points', sa.Integer(), nullable=True),
    sa.Column('delivered_points', sa.Integer(), nullable=True),
    sa.Column('started_points', sa.Integer(), nullable=False),
    sa.Column('sprint_issues', sa.String(length=500), nullable=True),
    sa.Column('sprint_risks', sa.String(length=500), nullable=True),
    sa.Column('sprint_dependencies', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sprints')
    ### end Alembic commands ###
