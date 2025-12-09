#Hands on with time
import time

def timeprint() -> None:
    print("Timer started")
    time.sleep(2)
    print("First 2 seconds done")
    time.sleep(2)
    print("First 4 seconds done")
    time.sleep(2)
    print("First 6 seconds done")
    print("Done. Total time: 6 seconds")
# timeprint()

#Now this took 6 seconds as we waited for 2 seconds in each step sequentially.
#This can be a problem when we are using HTTP requests or other I/O operations that can take time.
#To solve this problem, we can use asynchronous programming.
#Asynchronous programming allows us to run multiple tasks concurrently, making better use of time.
#Async != Multithreading, it is reallocatoin of cpu when one code is blocked waiting for I/O operation to complete.
#This can only be done in functions or code which are not CPU bound. If the code is CPU bound, then we need to use multiprocessing or multithreading.
#Async is more efficient than multithreading as it does not require context switching between threads.

import asyncio 
async def printasync() -> None:
    print("Async started")
    await  asyncio.sleep(2)
    print("First 2 seconds done")
    await asyncio.sleep(2)
    print("First 4 seconds done")
    await asyncio.sleep(2)
    print("First 6 seconds done")   
    print("Done. Total time: 6 seconds")
    print("But wait this was async!")
    
    
    
async def slow_square(n : int) -> int:
    print(f"This task is for {n}")
    await asyncio.sleep(5) #This wont work if its time.sleep(2)
    print(f"Task for {n} is done")
    return n*n

async def main_runner() -> None:
    #This is the main function which will create us te eventloop which will inreturn habdle all the coroutines and executions
    r1= await slow_square(3)
    print(r1)
    r2 = await slow_square(4)
    print(r2)
    #The above two calls are sequential and will take 4 seconds in total.
    
    thread1 =  asyncio.create_task(slow_square(5))
    thread2 =  asyncio.create_task(slow_square(6))
    r3 = await thread1
    print(r3)
    r4 = await thread2
    print(r4)
    #The above two calls are concurrent and will take only 2 seconds in total.
    
    r5, r6 = await asyncio.gather(slow_square(7), slow_square(8))
    print(r5)
    print(r6)
#The main thing which we want to note here is that it will yeild back to the I/O (blocked lines), and start another task.
#But this is still sequencial where first IO code is still executed in same sequence
    
# asyncio.run(main_runner())
#It really matters where we write the await keyword.

async def fetch1()-> None:
    print("This is fetch 1")
    await asyncio.sleep(3)
    print("This is fetch 1")
async def fetch2()-> None:
    print("This is fetch 2")
    await asyncio.sleep(3)
    print("This is fetch 2")
async def fetch3()-> None:
    print("This is fetch 3")
    await asyncio.sleep(3)
    print("This is fetch 3")
async def fetch4()-> None:
    print("This is fetch 4")
    await asyncio.sleep(3)
    print("This is fetch 4")
async def fetch5()-> None:
    print("This is fetch 5")
    await asyncio.sleep(1)
    print("This is fetch 5")
async def main():
    await fetch1()
    await fetch2()
    await fetch3()
    await fetch4()
    await fetch5()
    await asyncio.gather(fetch1(), fetch2(),fetch3(),fetch4(),fetch5())

asyncio.run(main())
