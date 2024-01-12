import uvicorn
from fastapi import FastAPI
from app import routers


app = FastAPI(title="TEXTAPI", version="1.1.1")

app.include_router(routers.router, prefix="")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, debug=False)
