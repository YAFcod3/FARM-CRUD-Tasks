
from fastapi import APIRouter,HTTPException
from models import Task,UpdateTask
from database import get_all_tasks,create_task,get_one_task,get_one_task_id,delete_task,update_task


route_task=APIRouter()


@route_task.get('/api/tasks')
async def get_tasks():
  tasks=await get_all_tasks()
  return tasks



@route_task.post('/api/tasks',response_model=Task)
async def save_task(task:Task):
  #para no repetir la tarea
  taskFound=await get_one_task(task.title)
  if taskFound:
    raise HTTPException(400,'Task already exists')
  else:
    # print(task)
    response = await create_task(task.dict())
    if response:
    #  print(response)
     return response
    raise HTTPException(400,'Something went wrong')


  




@route_task.get('/api/tasks/{id}',response_model=Task)
async def get_task(id:str):
  task= await get_one_task_id(id)
  if task:
    return task
  else:
    raise HTTPException(404,f'Task with ${id} not found')




@route_task.put('/api/tasks/{id}',response_model=Task)
async def put_task(id:str,task:UpdateTask):
  response=await update_task(id,task)
  if response:
    return response
  return HTTPException(404,f'Task with ${id} not found')






@route_task.delete('/api/tasks/{id}')
async def remove_task(id:str):
  response= await delete_task(id)
  if response:
    return "Successfully deleted task"
  else:
    raise HTTPException(404,f'Task with ${id} not found')