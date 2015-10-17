"""empty message

Revision ID: f140c10195
Revises: 35a1a19beae
Create Date: 2015-10-17 21:29:27.167357

"""

# revision identifiers, used by Alembic.
revision = 'f140c10195'
down_revision = '35a1a19beae'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sprintpeople', 'person_name',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=100),
               existing_nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sprintpeople', 'person_name',
               existing_type=sa.String(length=100),
               type_=sa.INTEGER(),
               existing_nullable=False)
    ### end Alembic commands ###
