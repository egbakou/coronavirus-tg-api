"""
app.main.py
"""
import logging
import os
from urllib.request import Request

import pydantic
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse

from .routers import V1
from .utils.httputils import setup_client_session, teardown_client_session

# ############
# FastAPI App
# ############
LOGGER = logging.getLogger("api")

APP = FastAPI(
    title="Coronavirus Tracker for Togo",
    description=(
        "API for tracking the coronavirus (COVID-19, SARS-CoV-2) outbreak in Togo."
        " Project page: https://github.com/egbakou/coronavirus-tg-api."
    ),
    version="1.0.0",
    docs_url="/",
    redoc_url="/docs",
    on_startup=[setup_client_session],
    on_shutdown=[teardown_client_session],
)

# #####################
# Middleware
#######################

# Enable CORS.
APP.add_middleware(
    CORSMiddleware, allow_credentials=True, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)
APP.add_middleware(GZipMiddleware, minimum_size=1000)

# ################
# Exception Handler
# ################


@APP.exception_handler(pydantic.error_wrappers.ValidationError)
async def handle_validation_error(
    request: Request, exc: pydantic.error_wrappers.ValidationError
):  # pylint: disable=unused-argument
    """
    Handles validation errors.
    """
    return JSONResponse({"message": exc.errors()}, status_code=422)


# ################
# Routing
# ################


# Include routers.
APP.include_router(V1, prefix="v1", tags=["v1"])


# Running of app.
if __name__ == "__main__":
    uvicorn.run(
        "app.main:APP", host="127.0.0.1", port=int(os.getenv("PORT", "5000")), log_level="info",
    )
