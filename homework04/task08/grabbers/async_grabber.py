import asyncio
import aiohttp

__all__ = ['AsyncGrabber']


class AsyncGrabber:

    def __init__(self):
        self._storage = []

    @property
    def storage(self) -> list[str]:
        return self._storage

    def drop_storage(self):
        self._storage = []

    async def obtain_page(self, url: str = None):
        user_agent = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=user_agent) as response:
                data = await response.text()
                self._storage.append(data)

    async def tasker(self, link_list: list) -> bool:
        tasks = [asyncio.create_task(self.obtain_page(link)) for link in link_list]
        await asyncio.gather(*tasks)

        return True

    def multi_grabber(self, link_list: list):

        asyncio.run(self.tasker(link_list))

        if self._storage:
            return True
        return False
