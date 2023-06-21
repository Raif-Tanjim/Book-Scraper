import asyncio
import aiohttp
import async_timeout
import requests
import time
from pages.Books_pages import Bookspage
from csv import writer

page_content = requests.get('https://books.toscrape.com').content
page = Bookspage(page_content)
loop = asyncio.get_event_loop()
books = page.books


async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(20):
        async with session.get(url) as response:
            print(f" Time took {time.time() - page_start}")
            return await response.text()


async def get_multiple_pages(loop, urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


urls = ['https://books.toscrape.com/catalogue/page-{page_num + 1}.html' for page_num in range(1, page.page_count)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, urls))
print(f"Full time = {time.time() - start}")

for page_content in pages:
    page = Bookspage(page_content)
    books.extend(page.books)

# extra
book_tup = [({book.name}, {book.rating}, {book.price}, {book.link}) for book in books]

with open('books.csv', 'w', newline='') as file:
    writer = writer(file)
    writer.writerow(['Name', 'Rating', 'Price', 'Link'])
    writer.writerows(book_tup)
