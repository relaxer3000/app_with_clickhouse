from faststream import FastStream
from faststream.rabbit import RabbitBroker

from config.settings import settings
from configurate import ocm
from rabbit.publisher import queue


broker = RabbitBroker(url=settings.rabbit_url)
app = FastStream(broker)


@broker.subscriber(queue)
async def insert_in_chdb(msg) -> None:
    ocm.insert_user(msg)
