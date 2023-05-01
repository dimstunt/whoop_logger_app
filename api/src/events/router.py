import time

from fastapi import APIRouter, Depends, HTTPException
# from fastapi_cache.decorator import cache
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from events.models import event
from events.schemas import EventCreate, EventType

router = APIRouter(
    prefix="/events",
    tags=["event"]
)


@router.get("")
async def get_specific_operations(
        event_type: str = EventType.SLEEP,
        session: AsyncSession = Depends(get_async_session),
):
    try:
        query = select(event).where(event.c.type == event_type)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.all(),
            "details": None
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/main")
async def main(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(1))
    return result.all()