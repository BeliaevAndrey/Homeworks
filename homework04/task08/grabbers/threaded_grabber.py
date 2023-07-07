import threading
import requests
from time import sleep

__all__ = ["ThreadedGrabber"]


class ThreadedGrabber:

    def __init__(self):
        self._storage = []

    @property
    def storage(self) -> list[str]:
        return self._storage

    def drop_storage(self):
        self._storage = []

    @staticmethod
    def obtain_page(url: str = None):
        try:
            return requests.get(url).text
        except Exception as exc:
            print(f'\033[31m{exc.__class__.__name__}: {exc}\033[0m')
            return "ConnectionError"

    def get_data(self, url, storage: list):
        text = self.obtain_page(url)
        if text != "ConnectionError":
            storage.append(text)
        else:
            sleep(0.5)

    def multi_grabber(self, link_list: list) -> bool:
        threads = []
        for link in link_list:
            t = threading.Thread(target=self.get_data, args=(link, self._storage))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return True
