import re
from bs4 import BeautifulSoup

from locators.book_page_locator import Bookspagelocator
from parsers.Books_parser import BookParser


class Bookspage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')
    @property
    def books(self):
        locator = Bookspagelocator.Books
        book = self.soup.select(locator)
        return [BookParser(e) for e in book]

    @property
    def page_count(self):
        content = self.soup.select_one(Bookspagelocator.pager).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        return pages
