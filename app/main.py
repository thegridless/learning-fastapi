from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Status(BaseModel):
    status: str = "ok"


@app.get("/")
async def get():
    return Status()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
