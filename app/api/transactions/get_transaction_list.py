import sqlalchemy as sa
from sqlalchemy.orm import Session

from app.api_models import BaseResponseModel
from app.api_models.transaction_model import TransactionModel
from app.models.transaction import Transaction
from app.utils.db import db_engine


class GetTransactionListResponseModel(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': [
                    {
                    'id': 1,
                    'created_at': '2021-11-06 13:25',
                    'status': 10,
                    'total': 400
                    }
                ],
                'meta': {},
                'success': True,
                'code': 200,
                'message': 'Success'
            }
        }


async def get_transaction_list():
    with Session(db_engine) as session:
        transaction_list = session.query(
            Transaction
        ).order_by(
            sa.desc(Transaction.id)
        ).all()

        result = []

        for transaction in transaction_list:
            result.append(
                TransactionModel(
                    id=transaction.id,
                    created_at=transaction.created_at,
                    status=transaction.status,
                    total=transaction.total
                )
            )

        return GetTransactionListResponseModel(
            data=result
        )
