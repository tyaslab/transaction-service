import sqlalchemy as sa
from app.models import Base


class TransactionItem(Base):
    __tablename__ = 'TransactionItem'

    id = sa.Column('id', sa.Integer, primary_key=True)
    user_id = sa.Column('user_id', sa.Integer)
    transaction_id = sa.Column('transaction_id', sa.Integer)
    created_at = sa.Column('created_at', sa.DateTime, default=sa.func.NOW())
    modified_at = sa.Column('modified_at', sa.DateTime, default=sa.func.NOW(), onupdate=sa.func.NOW())
    product_id = sa.Column('product_id', sa.Integer)
    product_name = sa.Column('product_name', sa.String)
    price = sa.Column('price', sa.Integer)
    qty = sa.Column('qty', sa.Integer)
    total = sa.Column('total', sa.Integer)
