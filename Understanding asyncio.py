#asyncio is Python’s built-in library for asynchronous programming, enabling efficient handling of I/O-bound tasks like web scraping, API requests, and database operations.
#It uses an event loop to manage coroutines efficiently.

#COROUTINE
"""A coroutine is a special type of function declared with async def. 
It can be paused and resumed using await."""

import asyncio
import time

async def greet():
    print("Hello")
    await asyncio.sleep(1)  # Non-blocking pause, allowing other coroutines to run.
    print("World") #world will be printed after 5 seconds

asyncio.run(greet())  # Runs the coroutine

"""Now let's run multiple coroutines together"""

async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)  # Simulating an I/O operation
    print(f"Task {name} completed")

async def main():
    await asyncio.gather(task("A", 5), task("B", 1))  # Run both coroutines concurrently

asyncio.run(main())
#Here task A will start first. Then task B will start. 
#Task B will be completed first due to its less delay.

#RUNNING COROUTINES INDEPENDENTLY

async def task1(): #Task 1 definition
    print("task 1 started")
    await asyncio.sleep(4)
    print("Task 1 done")

async def task2(): ##Task 2 definition
    print("task 2 started")
    await asyncio.sleep(2)
    print("Task 2 done")

async def main():
    t1 = asyncio.create_task(task1())  # Runs task1 independently
    t2 = asyncio.create_task(task2())  # Runs task2 independently
    await t1  # Wait for task1 to finish
    await t2  # Wait for task2 to finish
start_time = time.time()
asyncio.run(main())
time_taken = time.time() - start_time
print(time_taken)
#create_task() starts tasks immediately, while gather() waits for them.


