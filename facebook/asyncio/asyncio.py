import asyncio
import time

async def f(semaphore):
    await semaphore.acquire()
    await time.sleep(3)
    semaphore.release()

async def main(loop):
    sm = asyncio.Semaphore(value=2);
    await asyncio.wait([f(sm),f(sm),f(sm)])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
