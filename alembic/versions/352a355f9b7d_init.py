"""init

Revision ID: 352a355f9b7d
Revises: 
Create Date: 2022-10-14 23:41:30.622063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '352a355f9b7d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'ads',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String),
        sa.Column('amount', sa.Integer),
        sa.Column('price', sa.Integer),
        sa.Column('material', sa.String)
    )
    pass


def downgrade() -> None:
    op.drop_table('ads')
    pass