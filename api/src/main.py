from fastapi import FastAPI

from events.schemas import router as router_operation

app = FastAPI(
    title="Whoop logger"
)


@app.get("/ping")
def pong():
    return {"ping": "pong!"}

# app.include_router(router_operation)
