from fastapi import FastAPI
from client.config.config import app_name, host, port, reload
from client.run import start_app
from routers.router import router

app = FastAPI(lifespan=start_app)
app.include_router(router=router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app_name,host=host, port=port, reload=reload)