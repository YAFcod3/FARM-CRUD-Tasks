from fastapi import FastAPI,HTTPException
from routes.task import route_task




app=FastAPI()

@app.get('/')
def welcome():
  return {'message':'welcome to the my FastApi API'}


app.include_router(route_task)
