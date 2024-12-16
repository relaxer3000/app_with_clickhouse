import asyncio

from rabbit.publisher import declare_rabbit


async def try_connect_to_rabbit():
    retries = 5
    while retries > 0:
        try:
            await declare_rabbit()
            break
        except Exception as exc:
            print(f"Connection failed: {exc}. Retrying...")
            retries -= 1

            if retries == 0:
                print("Max retries exceeded. Could not connect to RabbitMQ.")
                raise

            await asyncio.sleep(5)
