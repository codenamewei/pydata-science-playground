from time import time
import asyncio
import random

def create_time():
    return random.choice(list(range(1, 5)))

async def task1():
    print("[TASK1] Start...")
    await asyncio.sleep(create_time()) 
    print("End...  [TASK1]")

async def task2():
    print("[TASK2] Start...")
    await asyncio.sleep(create_time()) 
    print("End...  [TASK2]")

async def task3():
    print("[TASK3] Start...")
    await asyncio.sleep(create_time()) 
    print("End...  [TASK3]")

async def runalltasks():

    start_time = time()
    run_task1 = asyncio.create_task(task1())
    run_task2 = asyncio.create_task(task2())
    run_task3 = asyncio.create_task(task3())

    print(">>> Start")
    await run_task1
    await run_task2
    await run_task3
    print(">>> End")

    end_time = time()
    print(f"Total time to make breakfast: {end_time - start_time} seconds.")

if __name__ == "__main__":
    asyncio.run(runalltasks())