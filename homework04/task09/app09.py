import requests
import threading
import multiprocessing

from async_downloader import async_way
from t08_util import timer_dec


@timer_dec
def threaded_way(links_list: list):
    threads = []
    for url in links_list:
        thread = threading.Thread(target=downloader, args=(url, 'threads',))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


@timer_dec
def processed_way(links_list: list):
    processes = []
    for url in links_list:
        process = multiprocessing.Process(target=downloader, args=(url, 'processes',))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


@timer_dec
def downloader(url: str, sub_path: str):
    file_name = url.rsplit('/', 1)[1]
    data = requests.get(url)
    if data.status_code == 200:
        with open(f'download/{sub_path}/{file_name}', 'wb') as f_out:
            for chunk in data:
                f_out.write(chunk)
    else:
        print(f'Data wasn\'t obtained {data.status_code=}')


@timer_dec
def main():
    with open('img_links.txt', 'r', encoding='utf-8') as f_in:
        links = f_in.read().split()
    threaded_way(links)
    print('\n', '=' * 80)
    processed_way(links)
    print('\n', '=' * 80)
    async_way(links)


if __name__ == '__main__':
    main()
