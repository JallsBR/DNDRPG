"""empty message

Revision ID: be28cbe5c648
Revises: 4aac55a469e9
Create Date: 2024-10-08 23:13:21.943843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be28cbe5c648'
down_revision = '4aac55a469e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('magias', schema=None) as batch_op:
        batch_op.add_column(sa.Column('magia', sa.JSON(), nullable=False))
        batch_op.drop_column('efeito_nd')
        batch_op.drop_column('level')
        batch_op.drop_column('nome_original')
        batch_op.drop_column('escola')
        batch_op.drop_column('tempo')
        batch_op.drop_column('descrição')
        batch_op.drop_column('componentes')
        batch_op.drop_column('descrição_original')
        batch_op.drop_column('alcance')
        batch_op.drop_column('duracao')
        batch_op.drop_column('livro')
        batch_op.drop_column('nome')
        batch_op.drop_column('classes')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('magias', schema=None) as batch_op:
        batch_op.add_column(sa.Column('classes', sa.VARCHAR(length=120), nullable=False))
        batch_op.add_column(sa.Column('nome', sa.VARCHAR(length=40), nullable=False))
        batch_op.add_column(sa.Column('livro', sa.VARCHAR(length=120), nullable=False))
        batch_op.add_column(sa.Column('duracao', sa.VARCHAR(length=120), nullable=False))
        batch_op.add_column(sa.Column('alcance', sa.VARCHAR(length=120), nullable=False))
        batch_op.add_column(sa.Column('descrição_original', sa.TEXT(), nullable=True))
        batch_op.add_column(sa.Column('componentes', sa.VARCHAR(length=120), nullable=False))
        batch_op.add_column(sa.Column('descrição', sa.TEXT(), nullable=False))
        batch_op.add_column(sa.Column('tempo', sa.VARCHAR(length=120), nullable=False))
        batch_op.add_column(sa.Column('escola', sa.VARCHAR(length=120), nullable=False))
        batch_op.add_column(sa.Column('nome_original', sa.VARCHAR(length=40), nullable=False))
        batch_op.add_column(sa.Column('level', sa.INTEGER(), nullable=False))
        batch_op.add_column(sa.Column('efeito_nd', sa.VARCHAR(length=150), nullable=False))
        batch_op.drop_column('magia')

    # ### end Alembic commands ###
