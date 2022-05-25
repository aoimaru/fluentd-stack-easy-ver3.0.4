import uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.get("/v1/users/{user_id}")
def users(user_id):
    user = {
        "user_id":user_id
    }
    return user


if __name__ == "__main__":
    uvicorn.run(app, port=8000, loop="asyncio")