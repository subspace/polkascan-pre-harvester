"""Index hash council motion

Revision ID: 0bde1522ffb7
Revises: 03853c25f85a
Create Date: 2019-12-11 12:00:37.908125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bde1522ffb7'
down_revision = '03853c25f85a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_data_council_motion_motion_hash'), 'data_council_motion', ['motion_hash'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_data_council_motion_motion_hash'), table_name='data_council_motion')
    # ### end Alembic commands ###