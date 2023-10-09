## Python - Async
### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- async and await syntax
- How to execute an async program with asyncio
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the random module

```py
import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
```


The order of this output is the heart of async IO. Talking to each of the calls to count() is a single event loop, or coordinator. When each task reaches await asyncio.sleep(1), the function yells up to the event loop and gives control back to it, saying, “I’m going to be sleeping for 1 second. Go ahead and let something else meaningful be done in the meantime.”

The event loop then looks around and says, “Hey, I’ve got some other stuff I can do while you’re sleeping, so I’ll go ahead and do that.” It then looks at the other tasks and sees that they’re also waiting for something, so it goes ahead and starts those tasks as well. This is the essence of concurrency.

When the event loop finishes with the first task, it checks to see if it’s done sleeping. If it is, then it goes ahead and finishes the task. If not, then it moves on to the next task and starts working on that one. This continues until all of the tasks are done.

### Reference
[Async-io-python](https://realpython.com/async-io-python/)
[asyncio.html](https://docs.python.org/3/library/asyncio.html)
[random.uniform](https://docs.python.org/3/library/random.html#random.uniform)
[coroutines using async/await keywords](https://docs.python.org/3/library/asyncio-task.html#coroutine)
