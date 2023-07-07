import multiprocessing
import requests
from time import sleep

__all__ = ["ProcessedGrabber"]


class ProcessedGrabber:
    manager = multiprocessing.Manager()

    def __init__(self):
        self._storage = self.manager.list()

    @property
    def storage(self) -> list[str]:
        return self._storage

    def drop_storage(self):
        self._storage = self.manager.list()

    @staticmethod
    def obtain_page(url: str = None):
        try:
            return requests.get(url).text
        except Exception as exc:
            print(f'\033[31m{exc.__class__.__name__}: {exc}\033[0m')
            return "ConnectionError"

    def get_data(self, url):
        text = self.obtain_page(url)
        if text != "ConnectionError":
            self._storage.append(text)
        else:
            sleep(0.5)

    def multi_grabber(self, link_list: list) -> bool:
        processes = []
        for link in link_list:
            p = multiprocessing.Process(target=self.get_data, args=(link,))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        return True
