from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
playtime_db = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/update")
async def update_playtime(request: Request):
    data = await request.json()
    user_id = str(data["userId"])
    playtime = int(data["playtime"])
    playtime_db[user_id] = playtime_db.get(user_id, 0) + playtime
    return {"totalPlaytime": playtime_db[user_id]}

@app.get("/get/{user_id}")
async def get_playtime(user_id: str):
    return {"totalPlaytime": playtime_db.get(user_id, 0)}
