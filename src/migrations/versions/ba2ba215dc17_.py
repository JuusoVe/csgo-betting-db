"""empty message

Revision ID: ba2ba215dc17
Revises: 41281de9e92c
Create Date: 2022-01-07 12:10:50.306265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba2ba215dc17'
down_revision = '41281de9e92c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('player', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('player', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('player', 'updated_at')
    op.drop_column('player', 'created_at')
    # ### end Alembic commands ###
