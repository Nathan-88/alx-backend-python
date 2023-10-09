#!/usr/bin/env python3
"""an asynchrous coroutine that tasks in an integer argument
that waits for a random delay btw 0 and max_delay and
returns it"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """an asynchrous coroutine that tasks in an integer argument that
    waits for a random delay btw 0 and max_delay and returns it"""
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
