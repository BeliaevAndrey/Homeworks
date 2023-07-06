import asyncio
import aiohttp
from t08_util import timer_dec

__all__ = ['async_way']


@timer_dec
async def __downloader(url: str, sub_path: str):
    file_name = url.rsplit('/', 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(f'download/{sub_path}/{file_name}', 'wb') as fd:
                async for chunk in response.content.iter_chunked(512):
                    fd.write(chunk)


@timer_dec
async def __start_async(links: list):
    tasks = [asyncio.create_task(__downloader(link, 'async')) for link in links]
    await asyncio.gather(*tasks)


@timer_dec
def async_way(links: list):
    asyncio.run(__start_async(links))
