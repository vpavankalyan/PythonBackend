from fastapi import FastAPI
from common.models import Base
from common.database import engine
from routes.products import router as product_router
import uvicorn

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(product_router)

if __name__ == "__main__":
    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=5000,
        log_level="info"
    )
    server = uvicorn.Server(config)
    server.run()
