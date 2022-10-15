"""init

Revision ID: cf3a1a8af36a
Revises: 352a355f9b7d
Create Date: 2022-10-15 18:45:18.606781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf3a1a8af36a'
down_revision = '352a355f9b7d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'ads',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('uuid', sa.Integer, primary_key=True, index=False),
        sa.Column('name', sa.String),
        sa.Column('amount', sa.Integer),
        sa.Column('price', sa.Integer),
        sa.Column('material', sa.String)
    )
    pass


def downgrade() -> None:
    op.drop_table('ads')
    pass
