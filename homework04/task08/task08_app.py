# Задание No8
# 🐀 Напишите программу, которая будет скачивать страницы из списка URL-адресов и
#    сохранять их в отдельные файлы на диске.
# 🐀 В списке может быть несколько сотен URL-адресов.
# 🐀 При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# 🐀 Представьте три варианта решения.


import re
import os
from typing import TypeAlias

from grabbers import (ThreadedGrabber,
                      ProcessedGrabber,
                      AsyncGrabber, )

from t08_util import timer_dec, check_path

Grabber: TypeAlias = [ThreadedGrabber, ProcessedGrabber, AsyncGrabber]


class PageScrapper:

    def __init__(self, out_path: str, url, grabber: Grabber, links_limit: int = 300):
        """
        :param out_path: str    -- a path where to save a file
        :param url: str         -- sets a basic url to work with
        :param grabber: object  -- a grabber object to use for walking over a site
        :param links_limit: int -- upper limit of links to walk over
        """
        self._basic_url = url
        self.grabber = grabber
        self.out_path = check_path(out_path)
        self.links_limit = links_limit

    @property
    def path(self) -> str:
        return self.out_path

    def collect_links(self, page_content, key: str = 'letter') -> list[str]:
        """
        Collecting links from page. Based on regex.
        :param page_content: str    -- page content
        :param key: str             -- key determining a type of link (an index one or an item one)
        :return: list[str]          -- collected links list
        """
        pattern_letter = re.compile(r"<a class='chara' href='letter\.php\?charkod=[\d]+'>")
        pattern_word = re.compile(r"<a class='chara' href='word\.php\?wordid=[\d]+'>")
        if key == 'words':
            link_list = pattern_word.findall(page_content)
        else:
            link_list = pattern_letter.findall(page_content)

        for i in range(len(link_list)):
            link_list[i] = f'{self._basic_url}{link_list[i][link_list[i].index("href=") + 6:-2]}'

        return link_list

    def page_walker(self, links_list: list[str], limit: int = None, step: int = 30):
        """
        Walks over a lis of links to grab down
        :param links_list: list[str]    -- list of links to walk over
        :param limit: int               -- upper limit of links to walk over
        :param step: int                -- amount of links in queue simultaneously
        :return:
        """
        if limit is None:
            limit = self.links_limit
        if limit == 0:
            limit = len(links_list)
        if len(links_list) <= step:
            if self.grabber.multi_grabber(links_list):
                self.file_writer()
        else:
            for i in range(0, limit, step):
                if self.grabber.multi_grabber(links_list[i:i + step]):
                    self.file_writer()

    def file_writer(self):
        """Write them down to disk"""
        pattern = re.compile(r"<title>[\w\s\-]+</title>")
        missed_count = 1
        for page in self.grabber.storage:
            try:
                file_name = os.path.join(self.out_path, (pattern.findall(page)[0][7:-39].replace(' ', '_') + '.html'))
            except IndexError:
                file_name = os.path.join(self.out_path, f'undefined_{missed_count}.html')
                missed_count += 1
            if file_name != os.path.join(self.out_path, '.html'):
                with open(file_name, 'w', encoding='utf-8') as f_out:
                    f_out.write(page)

    def starter(self):
        """Local 'main()', rules the process"""
        links_list = []
        if self.grabber.multi_grabber([self._basic_url]):
            links_list = self.collect_links(*self.grabber.storage)
            self.grabber.drop_storage()
            print('Index:', len(links_list))
        else:
            print('\033[31mCarrier lost. Exiting\033[0m')
            raise SystemExit
        if self.grabber.multi_grabber(links_list):
            links_list = []
            for page in self.grabber.storage:
                links_list.extend(self.collect_links(page_content=page, key='words'))
            print(f'Words:', len(links_list))
        self.page_walker(links_list)


@timer_dec
def main():
    basic_url = 'https://slovarozhegova.ru/'
    scrapper_threads = PageScrapper('downloads/threads/pages',
                                    basic_url,
                                    ThreadedGrabber(),
                                    links_limit=150,
                                    )
    scrapper_threads.starter()

    scrapper_processes = PageScrapper('downloads/processes/pages',
                                      basic_url,
                                      ProcessedGrabber(),
                                      links_limit=150,
                                      )
    scrapper_processes.starter()

    scrapper_async = PageScrapper('downloads/async/pages',
                                  basic_url,
                                  AsyncGrabber(),
                                  links_limit=150,
                                  )
    scrapper_async.starter()


if __name__ == '__main__':
    main()
