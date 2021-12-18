from fastapi import Header
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.api_models import BaseResponseModel
from app.models.transaction import Transaction
from app.utils.db import db_engine


class CreateTransactionResponseModel(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id': 1,
                    'url': '/api/v1/transactions/1'
                },
                'meta': {},
                'success': True,
                'code': 200,
                'message': 'Success'
            }
        }


async def create_transaction(user_id: int = Header(0, alias='X-Consumer-ID')):
    if user_id == 0:
        raise HTTPException(403, detail='Anda tidak punya hak akses')

    with Session(db_engine) as session:
        transaction = Transaction(user_id=user_id)
        session.add(transaction)
        session.commit()

        return CreateTransactionResponseModel(
            data={
                'id': transaction.id,
                'url': f'/api/v1/transactions/{transaction.id}'  # HATEOAS
            }
        )
