from main import books

USER_CHOICE = '''Enter one of the following
- 'b' to look at best books
- 'c' to look at cheapest books
- 'n' to look at next available book on the catalogue
- 'q' to quit

Enter your choice: '''



def best_books():
    best_book = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in best_book:
        print(book)


def cheapest_books():
    cheapest_book = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_book:
        print(book)
books_generator = (x for x in books)

def next_book():
    print(next(books_generator))

user_choices = {
    'b': best_books,
    'c': cheapest_books,
    'n': next_book
}
def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('please put an available command')
        user_input = input(USER_CHOICE)

menu()

