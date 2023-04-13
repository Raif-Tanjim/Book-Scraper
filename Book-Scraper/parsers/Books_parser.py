import re

from locators.books_locators import Books_locator


class BookParser:
    Ratings = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5

    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f' Book: {self.name}, rated: {self.rating} , Price: £{self.price}, Link : {self.link}'

    @property
    def name(self):
        locator = Books_locator.Name
        link = self.parent.select_one(locator).attrs['title']
        return link

    @property
    def link(self):
        locator = Books_locator.link
        item_link = self.parent.select_one(locator).attrs['href']
        return item_link

    @property
    def price(self):
        locator = Books_locator.price
        item_price = self.parent.select_one(locator).string
        pattern = '£([0-9]+.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return float(matcher.group(1))

    @property
    def rating(self):
        locator = Books_locator.rating
        tag = self.parent.select_one(locator)
        classes = tag.attrs['class']
        rating_class = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.Ratings.get(rating_class[0])
        return rating_number
