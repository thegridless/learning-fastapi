from fastapi import FastAPI, HTTPException
import uvicorn
from models.users import User
from database import USERS_DATABASE

app = FastAPI()

@app.get("/users", tags=["Users"])
async def get() -> list:
    return USERS_DATABASE


@app.post('/add_user', tags=["Users"])
async def add_user(User: User) -> User:
    for user in USERS_DATABASE:
        if user.username == User.username:
            raise HTTPException(detail=f"User {User.username} already exists", status_code=400)

    USERS_DATABASE.append(User)
    return User


@app.put("/edit_user", tags=["Users"])
async def edit_user(User: User):
    for index, user in enumerate(USERS_DATABASE):
        if user.username == User.username:
            USERS_DATABASE[index] = User
            return User
    raise HTTPException(detail=f"User {User.username} not found to edit", status_code=400)


@app.delete('/delete_user', tags=["Users"])
async def delete_user(username: str) -> User:
    for index, user in enumerate(USERS_DATABASE):
        if user.username == username:
            USERS_DATABASE.pop(index)
            return user
    raise HTTPException(detail=f"User {username} not found to delete", status_code=400)





if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
