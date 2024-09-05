import requests
import time

def wo_threading_func(urls):
    for url in urls:
        crawl(url, "without_threads.txt")

def crawl(url, dest):
    try:
        result = requests.get(url).text
        with open(dest, "a") as f:
            f.write(result)

    except requests.exceptions.RequestException:
        print("Error with URL check!")

def with_threading_func(urls):
    import threading

    threads = []
    for url in urls:
        th = threading.Thread(target=crawl, args=(url, "with_threads.txt"))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

urls = [
        "https://jsonplaceholder.typicode.com/comments/1",
        "https://jsonplaceholder.typicode.com/comments/2",
        "https://jsonplaceholder.typicode.com/comments/3"]

#urls = ["https://jsonplaceholder.typicode.com/comments/" + str(x) for x in range(30)]
a = time.time()
#with_threading_func(urls)
wo_threading_func(urls)
print(time.time()-a)