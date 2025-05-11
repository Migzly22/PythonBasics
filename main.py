import asyncio
from utils.PyLogger import PyLogger
from utils.FetchUtility import pyFetch

logs = PyLogger
async def fetchFunc():
    logs.info("Fetching Please Wait")
    try:
        data = await pyFetch.get('https://dummyj1son.com/users', params= { "limit" : 5})
        #Box transform Dictionary into an object
        logs.info(f"Output : {data}")
        
    except Exception as e:
        logs.error(e)

    print("DONE")
def main():
    asyncio.run(fetchFunc()) 
    logs.info("Done")


if __name__ == "__main__":
    main()

