"""empty message

Revision ID: d0dae8aa1e3d
Revises: 612a8ac8cf0a
Create Date: 2018-11-25 18:01:28.085712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0dae8aa1e3d'
down_revision = '612a8ac8cf0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('livro', sa.String(), nullable=True),
    sa.Column('autor', sa.String(), nullable=True),
    sa.Column('editora', sa.String(), nullable=True),
    sa.Column('cidade', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cidade'),
    sa.UniqueConstraint('livro')
    )
    op.drop_table('posts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('book')
    # ### end Alembic commands ###
