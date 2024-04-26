from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
import logging
from router import router as tasks_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    logger.info('База очищена')
    await create_tables()
    logger.info('База готова к работе')
    yield
    logger.info('Выключение')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)