from asyncHttp import AsyncHttp




class SummonerLeague(AsyncHttp):
    def __init__(self,riotToken) -> None:
        super().__init__(riotToken)

    async def challengers(self,queue:str):
        uri = f"/lol/league/v4/challengerleagues/by-queue/{queue}"
        return await self.asyncRequest('get',uri)
    
    async def grandmasters(self,queue:str):
        uri = f"/lol/league/v4/grandmasterleagues/by-queue/{queue}"
        return await self.asyncRequest('get',uri)
    
    async def masters(self,queue:str):
        uri = f"/lol/league/v4/masterleagues/by-queue/{queue}"
        return await self.asyncRequest('get',uri)
    
    async def league(self,leagueId:str):
        uri = f"/lol/league/v4/leagues/{leagueId}"
        return await self.asyncRequest('get',uri)
    
    async def summonerRank(self,summonerId:str):
        uri = f"/lol/league/v4/entries/by-summoner/{summonerId}"
        return await self.asyncRequest('get',uri)
    
    async def leagueEntries(self,queue:str,tier:str,division:str):
        uri = f"/lol/league/v4/entries/{queue}/{tier}/{division}"
        return await self.asyncRequest('get',uri)