import asyncio
import aiohttp
import sys
import random
import threading
from fake_useragent import UserAgent

async def send_request(session, target, request_type):
    try:
        headers = {
            'User-Agent': UserAgent().random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        if request_type.upper() == "GET":
            async with session.get(target, headers=headers) as response:
                status = response.status
        elif request_type.upper() == "POST":
            async with session.post(target, headers=headers, data={}) as response:
                status = response.status
        else:
            print(f"Unsupported request type: {request_type}")
            return

        print(f"Status code: {status}")
    except Exception as e:
        print(f"An error occurred: {e}")

async def main(target, request_type, threads):
    async with aiohttp.ClientSession() as session:
        while True:
            tasks = []
            for _ in range(threads):
                task = asyncio.create_task(send_request(session, target, request_type))
                tasks.append(task)

            await asyncio.gather(*tasks)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <target> <GET/POST> <threads>")
        sys.exit(1)

    target = sys.argv[1]
    request_type = sys.argv[2]
    threads = int(sys.argv[3])

    try:
        asyncio.run(main(target, request_type, threads))
    except KeyboardInterrupt:
        print("\nTeste de estresse interrompido pelo usuário.")
