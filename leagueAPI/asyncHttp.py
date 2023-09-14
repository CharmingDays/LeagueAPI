import aiohttp
from aiohttp.client_reqrep import ClientResponse


class HttpResponse(object):
    def __init__(self,response:ClientResponse) -> None:
        self.response = response

    @property
    def ok(self):
        return self.response.ok
    
    async def json(self):
        return await self.response.json()


    @property
    def status(self):
        return self.response.status
    


    def __del__(self):
        self.response.close()



class AsyncHttp(object):
    def __init__(self,riotToken,region='na1',match_region='americas') -> None:
        self.__region = region
        self.__match_region = match_region
        self.region_url = "https://{}.api.riotgames.com"
        self.token = riotToken
        self.headers = {"X-Riot-Token":riotToken}

    
    def change_token(self,newToken):
        self.token = newToken



    @property
    def current_region(self):
        return self.__region


    @property
    def current_match_region(self):
        return self.__match_region


    async def MatchAsyncRequest(self,method:str,uri:str):
        """
        Request function for Match API of League of Legends API
        """
        url = self.region_url.format(self.__match_region)+uri
        async with aiohttp.ClientSession() as session:
            async with session.request(method,url) as resp:
                await resp.read()
                return HttpResponse(resp)


    async def asyncRequest(self,method:str,uri:str):
        url = self.region_url.format(self.__region)+uri
        async with aiohttp.ClientSession() as session:
            async with session.request(method,url,headers=self.headers) as resp:
                await resp.read()
                return HttpResponse(resp)
            


