import uvicorn
from fastapi import FastAPI

from configurate import db_name, ch_ini, ocm
from rabbit.publisher import declare_rabbit
from routers.user import user_router


app = FastAPI()

app.include_router(user_router, prefix="/user")


@app.on_event("startup")
async def startup():
    ch_ini.create_database(db_name)
    ocm.create_tables()
    await declare_rabbit()


@app.on_event("shutdown")
async def shutdown():
    ch_ini.drop_database(db_name)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
