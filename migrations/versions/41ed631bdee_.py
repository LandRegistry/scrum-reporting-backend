"""empty message

Revision ID: 41ed631bdee
Revises: 2105f3d01d0
Create Date: 2015-10-15 21:26:24.442038

"""

# revision identifiers, used by Alembic.
revision = '41ed631bdee'
down_revision = '2105f3d01d0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('projects', 'project_description',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=2000),
               existing_nullable=True)
    op.alter_column('sprints', 'sprint_challenges',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=2000),
               existing_nullable=False)
    op.alter_column('sprints', 'sprint_deliverables',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=2000),
               existing_nullable=True)
    op.alter_column('sprints', 'sprint_dependencies',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=2000),
               existing_nullable=True)
    op.alter_column('sprints', 'sprint_goal',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=2000),
               existing_nullable=True)
    op.alter_column('sprints', 'sprint_issues',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=2000),
               existing_nullable=True)
    op.alter_column('sprints', 'sprint_risks',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=2000),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sprints', 'sprint_risks',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)
    op.alter_column('sprints', 'sprint_issues',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)
    op.alter_column('sprints', 'sprint_goal',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)
    op.alter_column('sprints', 'sprint_dependencies',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)
    op.alter_column('sprints', 'sprint_deliverables',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)
    op.alter_column('sprints', 'sprint_challenges',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=False)
    op.alter_column('projects', 'project_description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)
    ### end Alembic commands ###
