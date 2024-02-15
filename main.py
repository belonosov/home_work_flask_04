import threading
import time

import requests

url_user = input('Enter URL your picture: ')
urls = [url_user]


def download(urls):
    response = requests.get(urls)
    text_url = urls.split('/')
    filename = f"image_{text_url[-1]}"
    with open(f"users_pic/{filename}", 'w', encoding='utf-8') as file:
        file.write(response.text)


if __name__ == '__main__':
    threads = []
    start_time = time.time()

    for url in urls:
        thread = threading.Thread(target=download, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"{time.time() - start_time} seconds")
