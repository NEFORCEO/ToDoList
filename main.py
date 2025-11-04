from fastapi import FastAPI
from client.config.config import app_name, host, port, reload
from client.run import start_app


app = FastAPI(lifespan=start_app)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app_name,host=host, port=post, reload=reload)