# Задание No7
# 1.  Создать RESTful API для управления списком задач. Приложение должно использовать
#     FastAPI и поддерживать следующие функции:
#       * Получение списка всех задач.
#       * Получение информации о задаче по её ID.
#       * Добавление новой задачи.
#       * Обновление информации о задаче по её ID.
#       * Удаление задачи по её ID.
# 2.  Каждая задача должна содержать следующие поля:
#       * ID (целое число),
#       * Название (строка),
#       * Описание (строка),
#       * Статус (строка): "tоdo", "in progress", "done".
# 3.  Создайте модуль приложения и настройте сервер и маршрутизацию.
# 4.  Создайте класс Task с полями id, title, description и status.
# 5.  Создайте список tasks для хранения задач.
# 6.  Создайте функцию get_tasks для получения списка всех задач (метод GET).
# 7.  Создайте функцию get_task для получения информации о задаче по её ID (метод GET).
# 8.  Создайте функцию create_task для добавления новой задачи (метод POST).
# 9.  Создайте функцию update_task для обновления информации о задаче по её ID (метод PUT).
# 10. Создайте функцию delete_task для удаления задачи по её ID (метод DELETE).

import uvicorn
from typing import Optional

from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel, EmailStr

app = FastAPI()


class NewTask(BaseModel):
    title: str
    description: Optional[str]
    status: str


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str


tasks = []


@app.get("/tasks", response_model=list[Task])
async def get_tasks():
    return tasks


@app.get("/tasks/{item_id}", response_model=Task)
async def get_item_by_id(item_id: int):
    task = [task for task in tasks if task.id == item_id]
    if task:
        return task[0]
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks/", response_model=Task)
@app.post("/tasks/")
async def create_task(task: NewTask):
    new_id = 1
    if tasks:
        new_id = max(tasks, key=lambda x: x.id).id + 1
    if task.status.lower() not in ["todo", "in progress", "done"]:
        return {"message": f"Wrong status: '{task.status}'\nOnly 'tоdo', 'in progress' or 'done' statuses available."}
    tasks.append(added_task := Task(
        id=new_id,
        title=task.title.capitalize(),
        description=task.description.capitalize(),
        status=task.status.lower(),
    ))
    return added_task


@app.put("/tasks/{task_id}", response_model=Task)
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    upd_task = [t for t in tasks if t.id == task_id]
    if not upd_task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.status.lower() not in ["todo", "in progress", "done"]:
        return {"message": f"Wrong status: '{task.status}'\nOnly 'tоdo', 'in progress' or 'done' statuses available."}
    upd_task[0].title = task.title.capitalize()
    upd_task[0].description = task.description.capitalize()
    upd_task[0].status = task.status.lower()
    return upd_task


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    del_task = [t for t in tasks if t.id == task_id]
    if not del_task:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks.remove(del_task[0])
    return del_task[0]


if __name__ == "__main__":
    uvicorn.run(
        "task07:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
