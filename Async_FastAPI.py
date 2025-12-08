'''
This is for: Usage of Async in general and in fastAPI
Async we use when there are multiple waiting activities, like fetch from db or read file or wait for HTTP response
Multithread we use when there are many tasks which are IO bound but should share data bw each other
Multi processing we use when there are many processes needed to run and all of them are independent of each other
'''
'''
Async doesnt mean faster code, it means efficient usage of waiting time in IO bound Non-CPU dependent tasks
GIL: Global Interpreter lock will not allow more than 1 command from python is actively executing.
This Mutex will prevent any code which can alter the same memory at the same time. 
'''
from fastapi import FastAPI, BackgroundTasks
import httpx
import asyncio

app = FastAPI()

#Support Functions which can be anything which are used in the code
async def email(email:str)-> None:
    print("Email registered:",email)
async def logger(**log:str) -> None:
    print("Logger done:" + log)

#Endpoint creation, here we can create endpoints for the users to hit. These can be get push put etc.
@app.get("/basicSync")
async def getURLData():
    """
    Docstring for getURLData and mimic multiple http calls
    """
    async with httpx.AsyncClient() as client:
        '''
    The usage of gather here is to gather all the coroutines and run them in the event loop.
    This will preserve the order the way we have called the Async functins.
        '''
        r1,r2 = await asyncio.gather(
            client.get("https://jsonplaceholder.typicode.com/posts"),
            client.get("https://jsonplaceholder.typicode.com/users")
        )
    return {r1.status_code, r2.status_code}

@app.get("/multitaskSync")
async def getdata() -> str:

    #here there is need to get some datafrom and endpoint
    async with httpx.AsyncClient() as client:
        '''
        This is asyncio.as_completed()
        This is as same as gather, which can gather all the coroutines which we need to run in event loop
        But this does not preserve the order of execution. The fastest response will be yield
        and we do not wait for the preceeding coroutines, if they are still blocked
        '''
        r1, r2 = await asyncio.as_completed(
            client.get("https://jsonplaceholder.typicode.com/posts"),
            client.get("https://jsonplaceholder.typicode.com/users")
        )

        BackgroundTasks.add_task(email("vedanth@gmail.com"), logger(user="vedanth", status="success"))
        '''
        The use of backgroundTask is to make another thread where these background tasks will run.
        There are cases where user seeing response is more important than sending them instant email or logging their activity
        So in these cases we can simply add them as background task and skip these task and send user instant response
        This increase user experience. Feels faster and background tasks are run after returning response to the user.
        '''

        return str(r1.status_code) +str(r2.status_code)
    

'''
Here blocked means when the CPU is idle, like read file or wait for API response, 
In these cases we can do other task as CPU is idle. These cases are where FastAPI is most dominant
'''



