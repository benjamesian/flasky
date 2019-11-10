"""empty message

Revision ID: 7503a05abc73
Revises: 640c7b32aa80
Create Date: 2019-11-09 20:20:12.731153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7503a05abc73'
down_revision = '640c7b32aa80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    # ### end Alembic commands ###
