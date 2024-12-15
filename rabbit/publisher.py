from faststream.rabbit import RabbitBroker, RabbitQueue

from config.settings import settings

broker = RabbitBroker(url=settings.rabbit_url)

queue = RabbitQueue(
    name="app_queue",
    durable=True,
)


async def declare_rabbit():
    async with broker as br:
        await br.declare_queue(queue)


async def push_in_queue(message):
    async with broker as br:
        await br.publish(
            message=message,
            queue="app_queue",
        )
