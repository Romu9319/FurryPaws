"""empty message

Revision ID: 753e7aceac4f
Revises: edbe254db289
Create Date: 2023-08-29 19:14:13.026992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '753e7aceac4f'
down_revision = 'edbe254db289'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vet_favorite', schema=None) as batch_op:
        batch_op.drop_constraint('vet_favorite_user_id_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vet_favorite', schema=None) as batch_op:
        batch_op.create_unique_constraint('vet_favorite_user_id_key', ['user_id'])

    # ### end Alembic commands ###