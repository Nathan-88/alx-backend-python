#!/usr/bin/python3
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    
async def main():
    task1 = asyncio.create_task(
        say_after(4, 'hello'))

    task2 = asyncio.create_task(
        say_after(3, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed  of two tasks, task1
    # and task2, before proceeding with the rest of the code.
    # This allows other asynchronous operations to run in parallel
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())


# async def count():
#     print("One")
#     await asyncio.sleep(1)
#     print("Two")

# async def main():
#     await asyncio.gather(count(), count(), count())

# if __name__ == "__main__":
#     import time
#     s = time.perf_counter()
#     asyncio.run(main())
#     elapsed = time.perf_counter() - s
#     print(f"{__file__} executed in {elapsed:0.2f} seconds.")