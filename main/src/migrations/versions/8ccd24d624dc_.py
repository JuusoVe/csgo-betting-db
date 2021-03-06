"""empty message

Revision ID: 8ccd24d624dc
Revises: a7c0085e80f9
Create Date: 2022-01-02 17:47:48.366556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ccd24d624dc'
down_revision = 'a7c0085e80f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('match',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lan', sa.Boolean(), nullable=True),
    sa.Column('team_1_id', sa.Integer(), nullable=False),
    sa.Column('team_2_id', sa.Integer(), nullable=False),
    sa.Column('format', sa.String(length=3), nullable=True),
    sa.Column('map_1', sa.String(length=64), nullable=True),
    sa.Column('map_2', sa.String(length=64), nullable=True),
    sa.Column('map_3', sa.String(length=64), nullable=True),
    sa.Column('map_4', sa.String(length=64), nullable=True),
    sa.Column('map_5', sa.String(length=64), nullable=True),
    sa.Column('map_1_winner', sa.Integer(), nullable=True),
    sa.Column('map_2_winner', sa.Integer(), nullable=True),
    sa.Column('map_3_winner', sa.Integer(), nullable=True),
    sa.Column('map_4_winner', sa.Integer(), nullable=True),
    sa.Column('map_5_winner', sa.Integer(), nullable=True),
    sa.Column('match_winner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_1_id'], ['team.id'], ),
    sa.ForeignKeyConstraint(['team_2_id'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('player', sa.Column('nick_first_last', sa.String(length=128), nullable=False))
    op.create_unique_constraint(None, 'player', ['nick_first_last'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'player', type_='unique')
    op.drop_column('player', 'nick_first_last')
    op.drop_table('match')
    # ### end Alembic commands ###
