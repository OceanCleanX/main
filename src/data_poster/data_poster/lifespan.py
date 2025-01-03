from contextlib import asynccontextmanager

from fastapi import FastAPI

from .lib.node import get_node, cleanup_node


@asynccontextmanager
async def lifespan(app: FastAPI):
    await get_node()
    yield
    cleanup_node()
