from asyncHttp import AsyncHttp

class Summoner(AsyncHttp):
    def __init__(self,riotToken) -> None:
        super().__init__(riotToken)
        
    async def by_name(self,summonerName:str):
        uri = f'/lol/summoner/v4/summoners/by-name/{summonerName}'
        return await self.asyncRequest('get',uri)
        
    async def by_uuid(self,uuid:str):
        uri = f"/lol/summoner/v4/summoners/by-puuid/{uuid}"
        return await self.asyncRequest('get',uri)
        
    async def accountId(self,accId:str):
        uri = f"/lol/summoner/v4/summoners/by-account/{accId}"
        return await self.asyncRequest('get',uri)
    
    async def summonerId(self,Id:str):
        uri = f"/lol/summoner/v4/summoners/{Id}"
        return await self.asyncRequest('get',uri)
    
    

