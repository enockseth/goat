"""Fixed foreign key

Revision ID: f52751aff400
Revises: bf178b4433dc
Create Date: 2022-01-26 21:29:01.550664

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2


# revision identifiers, used by Alembic.
revision = 'f52751aff400'
down_revision = 'bf178b4433dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('isochrone_calculation_id_fkey', 'isochrone_calculation', schema='customer', type_='foreignkey')
    op.create_foreign_key(None, 'isochrone_calculation', 'user', ['user_id'], ['id'], source_schema='customer', referent_schema='customer', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'isochrone_calculation', schema='customer', type_='foreignkey')
    op.create_foreign_key('isochrone_calculation_id_fkey', 'isochrone_calculation', 'user', ['id'], ['id'], source_schema='customer', referent_schema='customer', ondelete='CASCADE')
    # ### end Alembic commands ###
