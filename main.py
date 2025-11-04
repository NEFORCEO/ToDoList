from fastapi import FastAPI
from client.config.config import app_name, host, port, reload
from client.run import start_app
from routers.get_router import get_router
from routers.post_router import post_router
from routers.put_router import put_router
from routers.delete_router import delete_router

app = FastAPI(lifespan=start_app)

app.include_router(router=get_router)
app.include_router(router=post_router)
app.include_router(router=put_router)
app.include_router(router=delete_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app_name,host=host, port=port, reload=reload)