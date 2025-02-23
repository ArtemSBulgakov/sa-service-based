__all__ = ["lifespan"]

import json
import os
from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import timeout
from pymongo.errors import ConnectionFailure

from src.logging_ import logger
from src.storages.mongo.models import document_models


async def setup_repositories() -> AsyncIOMotorClient:
    motor_client = AsyncIOMotorClient(
        os.getenv("DB"), connectTimeoutMS=5000, serverSelectionTimeoutMS=5000
    )

    # healthcheck mongo
    try:
        with timeout(1):
            server_info = await motor_client.server_info()
            server_info_pretty_text = json.dumps(server_info, indent=2, default=str)
            logger.info(f"Connected to MongoDB: {server_info_pretty_text}")
    except ConnectionFailure as e:
        logger.critical("Could not connect to MongoDB: %s" % e)

    mongo_db = motor_client.get_default_database()
    await init_beanie(database=mongo_db, document_models=document_models)
    return motor_client


@asynccontextmanager
async def lifespan(_app: FastAPI):
    # Application startup

    motor_client = await setup_repositories()

    yield

    # Application shutdown
    motor_client.close()
