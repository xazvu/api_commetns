import uvicorn
from fastapi import FastAPI

from routers.users import router as users_router
from db.engine import init_db
from db import models
from db.engine import engine

init_db()

app = FastAPI()
app.include_router(users_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    # models.Base.metadata.drop_all(bind=engine)
    uvicorn.run(app, host="127.0.0.1", port=8000)