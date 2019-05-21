import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core import config
from core import urls
from core.middlewares.database import database_middleware
from core.middlewares.settings import settings_middleware

app = FastAPI(title=config.PROJECT_NAME, openapi_url="/api/v1/openapi.json")

# CORS
origins = []

# Set all CORS enabled origins

if config.BACKEND_CORS_ORIGINS:
    origins_raw = config.BACKEND_CORS_ORIGINS.split(",")
    for origin in origins_raw:
        use_origin = origin.strip()
        origins.append(use_origin)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(urls.router)

app.middleware('http')(settings_middleware(app))
app.middleware('http')(database_middleware(app))


if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=8000, log_level="info", reload=True)
