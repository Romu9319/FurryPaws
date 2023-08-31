"""empty message

Revision ID: 1b74fa8000bd
Revises: 9a7283cd7dd5
Create Date: 2023-08-29 09:25:38.051121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b74fa8000bd'
down_revision = '9a7283cd7dd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=300), nullable=False),
    sa.Column('body', sa.String(length=3000), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('image', sa.String(length=3000), nullable=False),
    sa.Column('author', sa.String(length=200), nullable=False),
    sa.Column('category', sa.Enum('Salud', 'Bienestar', 'Belleza', name='category_enum'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=150), nullable=False),
    sa.Column('company_name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=2000), nullable=False),
    sa.Column('avatar', sa.String(length=2000), nullable=False),
    sa.Column('services', sa.String(length=2000), nullable=True),
    sa.Column('price_low', sa.Integer(), nullable=False),
    sa.Column('price_high', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('avatar'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('vet_favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('vet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vet_id'], ['vet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vet_review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=300), nullable=False),
    sa.Column('body', sa.String(length=3000), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('rate', sa.Enum('1', '2', '3', '4', '5', name='rate_enum'), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('vet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vet_id'], ['vet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('phone_number', sa.String(length=150), nullable=False))
        batch_op.add_column(sa.Column('avatar', sa.String(length=2000), nullable=False))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=200),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.create_unique_constraint(None, ['phone_number'])
        batch_op.create_unique_constraint(None, ['avatar'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('password',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.drop_column('avatar')
        batch_op.drop_column('phone_number')
        batch_op.drop_column('last_name')
        batch_op.drop_column('name')

    op.drop_table('vet_review')
    op.drop_table('vet_favorite')
    op.drop_table('vet')
    op.drop_table('post')
    # ### end Alembic commands ###