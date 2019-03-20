#!/usr/bin/env python

import sys
import asyncio

from typing import List


async def sleepprint(i: int):
    await asyncio.sleep(i)
    print(i, end=" ", flush=True)


async def sleepsort(l: List[int]):
    # Create all coroutines before starting them
    tasks = [asyncio.create_task(sleepprint(i)) for i in l]
    # Run coroutines
    for t in tasks:
        await t


if __name__ == "__main__":
    args = [int(val) for val in sys.argv[1:]]
    asyncio.run(sleepsort(args))
