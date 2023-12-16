"""empty message

Revision ID: e831989ce008
Revises: 76b47d880c57
Create Date: 2023-12-16 00:26:28.346551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e831989ce008'
down_revision = '76b47d880c57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('img', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('img'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('item')
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('item_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'items', ['item_id'], ['id'])

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('item_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'items', ['item_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('item_id')

    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('item_id')

    op.create_table('item',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('img', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='item_pkey'),
    sa.UniqueConstraint('description', name='item_description_key'),
    sa.UniqueConstraint('img', name='item_img_key'),
    sa.UniqueConstraint('name', name='item_name_key')
    )
    op.drop_table('items')
    # ### end Alembic commands ###
