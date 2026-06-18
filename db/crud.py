from datetime import datetime
from .models import User, Subscription
from sqlalchemy import select, update, delete, insert, func
from . import session_factory


# users ----------------------------------------------------------------------------------------------------------------
async def get_all_users() -> list[User]:
    async with session_factory() as session:
        result = await session.execute(
            select(User)
        )
        return result.scalars().all()


async def create_user(tg_id: int) -> None:
    async with session_factory() as session:
        await session.add(
            User(
                tg_id=tg_id,
                reg_date=datetime.now()
            )
        )
        await session.commit()


async def get_user_by_tg_id(tg_id: int) -> User:
    async with session_factory() as session:
        result = await session.execute(
            select(User).where(User.tg_id == tg_id)
        )
        return result.scalar()


# subs -----------------------------------------------------------------------------------------------------------------
async def get_all_user_subs_by_user_tg_id_with_join(user_tg_id: int) -> list[Subscription]:
    async with session_factory() as session:
        result = await session.execute(
            select(Subscription)
            .join(User, Subscription.user_id == User.id)
            .where(User.tg_id == user_tg_id)
        )
        return result.scalars().all()


async def get_all_user_subs_by_user_tg_id(user_tg_id: int) -> list[Subscription]:
    async with session_factory() as session:
        user = await session.execute(
            select(User).where(User.tg_id == user_tg_id)
        ).scalar()
        if not user:
            return []
        result = await session.execute(
            select(Subscription).where(Subscription.user_id == user.id)
        )
        return result.scalars().all()


async def create_sub_by_user_tg_id(
        from_station_id: int, to_station_id: int, origin_date: datetime, user_tg_id: int) -> None:
    async with session_factory() as session:
        user = await session.execute(
            select(User).where(User.tg_id == user_tg_id)
        ).scalar()
        if not user:
            return
        await session.add(Subscription(
            user_id=user.id,
            from_station_id=from_station_id,
            to_station_id=to_station_id,
            origin_date=origin_date
        ))
        await session.commit()


async def delete_sub_by_sub_id(sub_id: int) -> None:
    async with session_factory() as session:
        await session.execute(delete(Subscription).where(Subscription.id == sub_id))
        await session.commit()


async def delete_all_user_subs_by_user_tg_id(user_tg_id: int) -> None:
    async with session_factory() as session:
        await session.execute(delete(Subscription).where(Subscription.user_id == user_tg_id))
        await session.commit()
