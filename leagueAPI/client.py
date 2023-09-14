import asyncio
from summoner import Summoner
from league import SummonerLeague
from dotenv import load_dotenv
import os

load_dotenv()


class Client(Summoner,SummonerLeague):
    def __init__(self, riotToken) -> None:
        super().__init__(riotToken)




league = Client(os.getenv('RIOT_API_KEY'))
async def main():
    user = await league.by_name('cheng yue')

asyncio.run(main())