import asyncio
from utils.PyLogger import PyLogger as logs
from utils.FetchUtility import pyFetch
from config import API_URL


async def fetchFunc():
    logs.info("Fetching Please Wait")
    try:
        data = await pyFetch.get( API_URL, params= { "limit" : 5} )
        logs.info(f"Output : {data}")
        
    except Exception as e:
        logs.error(e)

def main():
    asyncio.run(fetchFunc()) 
    logs.info("Done")
    
if __name__ == "__main__":
    main()
