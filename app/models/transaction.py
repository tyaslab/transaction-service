import sqlalchemy as sa
from app.models import Base


class TransactionStatus:
    OUTSTANDING: int = 10
    COMPLETE: int = 20
    CANCELED: int = 30


class Transaction(Base):
    __tablename__ = 'Transaction'

    id = sa.Column('id', sa.Integer, primary_key=True)
    user_id = sa.Column('user_id', sa.Integer)
    created_at = sa.Column('created_at', sa.DateTime, default=sa.func.NOW())
    modified_at = sa.Column('modified_at', sa.DateTime, default=sa.func.NOW(), onupdate=sa.func.NOW())
    status = sa.Column('status', sa.Integer, default=TransactionStatus.OUTSTANDING)
    total = sa.Column('total', sa.Integer, default=0)
