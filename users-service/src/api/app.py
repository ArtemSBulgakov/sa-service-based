__all__ = ["app"]

from fastapi import FastAPI
from fastapi_swagger import patch_fastapi
from starlette.middleware.cors import CORSMiddleware

import src.logging_  # noqa: F401
from src.api.lifespan import lifespan

app = FastAPI(
    title="Users Service",
    root_path="/users",
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None,
    swagger_ui_oauth2_redirect_url=None,
)

patch_fastapi(app)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from src.modules.users.routes import router as router_users  # noqa: E402

app.include_router(router_users)
