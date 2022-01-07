"""empty message

Revision ID: ed2322d6e50f
Revises: 2449eef34aed
Create Date: 2022-01-07 13:10:08.091191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed2322d6e50f'
down_revision = '2449eef34aed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('team_organization_name_fkey', 'team', type_='foreignkey')
    op.drop_constraint('team_organization_id_fkey', 'team', type_='foreignkey')
    op.drop_column('team', 'organization_id')
    op.drop_column('team', 'organization_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team', sa.Column('organization_name', sa.VARCHAR(length=64), autoincrement=False, nullable=False))
    op.add_column('team', sa.Column('organization_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('team_organization_id_fkey', 'team', 'organization', ['organization_id'], ['id'])
    op.create_foreign_key('team_organization_name_fkey', 'team', 'organization', ['organization_name'], ['name'])
    # ### end Alembic commands ###
