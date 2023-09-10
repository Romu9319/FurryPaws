"""empty message

Revision ID: 8c1d437e63be
Revises: a767cf1ce8b3
Create Date: 2023-09-07 10:47:37.664568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c1d437e63be'
down_revision = 'a767cf1ce8b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vet', schema=None) as batch_op:
        batch_op.drop_constraint('vet_avatar_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vet', schema=None) as batch_op:
        batch_op.create_unique_constraint('vet_avatar_key', ['avatar'])

    # ### end Alembic commands ###
