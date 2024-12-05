import time
import threading
import requests
import aiohttp
import asyncio


from threading import Thread

# Threading
class ThreadingDownloader(threading.Thread):
    json_array = []

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        return self.json_array

def get_data_threading(urls):
    st = time.time()
    threads = []
    for url in urls:
        t = ThreadingDownloader(url)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        print(t)

    et = time.time()
    elapsed_time = et - st
    print("Execution time: ", elapsed_time, " seconds")

urls = ["http://postman-echo.com/delay/3"] * 10
#get_data_threading(urls)



#Async
async def get_data(session, url, json_array):
    async with session.get(url) as resp:
        json_array.append(await resp.json())

async def get_data_async_concurrently(urls):
    st = time.time()
    json_array = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get_data(session, url, json_array)))
        await asyncio.gather(*tasks)

    et = time.time()
    elapsed_time = et - st
    print("Execution time: ", elapsed_time, " second")
    return json_array

asyncio.run(get_data_async_concurrently(urls))







