from fastapi import APIRouter
from models import Order, OrderBillet
from database import db, orders
from typing import List

router = APIRouter()


@router.post("/orders/", response_model=Order)
async def add_order(order: OrderBillet):
    query = orders.insert().values(**order.dict())
    last_id = await db.execute(query)
    return {**order.dict(), "id": last_id}


@router.get("/orders/", response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await db.fetch_all(query)


@router.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await db.fetch_one(query)


@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderBillet):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
    await db.execute(query)
    return {**new_order.dict(), "id": order_id}


@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await db.execute(query)
    return {"message": "A order deleted"}
