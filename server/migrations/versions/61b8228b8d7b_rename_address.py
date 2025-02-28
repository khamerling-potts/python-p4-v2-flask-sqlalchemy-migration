"""rename address

Revision ID: 61b8228b8d7b
Revises: a5932fcae360
Create Date: 2024-01-18 12:47:51.031397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "61b8228b8d7b"
down_revision = "a5932fcae360"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("departments", "address", new_column_name="location")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("departments", "location", new_column_name="address")
    # ### end Alembic commands ###
