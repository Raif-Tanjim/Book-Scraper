import requests
from pages.Books_pages import Bookspage
from csv import writer
page_content = requests.get('https://books.toscrape.com').content
page = Bookspage(page_content)

books = page.books
for page_num in range(1, page.page_count):
    url = f'https://books.toscrape.com/catalogue/page-{page_num + 1}.html'
    page_content = requests.get(url).content
    page = Bookspage(page_content)
    books.extend(page.books)

book_tup = [({book.name}, {book.rating}, {book.price}, {book.link}) for book in books]

with open('books.csv', 'w', newline='') as file:
    writer = writer(file)
    writer.writerow(['Name', 'Rating', 'Price', 'Link'])
    writer.writerows(book_tup)
