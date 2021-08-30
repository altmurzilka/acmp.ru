class PageCountError(Exception):
    message = "Too many pages"

    def __init__(self):
        super().__init__(self.message)


class YearError(Exception):
    message = "Too old book"

    def __init__(self):
        super().__init__(self.message)


class AuthorError(Exception):
    message = "Incorrect author name"

    def __init__(self):
        super().__init__(self.message)


class PriceError(Exception):
    message = "Price is too high"

    def __init__(self, currnt_price, max_price):
        self.error_message = f"""{self.message}: current = {currnt_price},
                            max = {max_price}"""
        super().__init__(self.error_message)


class Book:
    def __init__(self, pages, year, author, price):
        self.pages = self.val_count(pages)
        self.year = self.val_year(year)
        self.author = self.val_author(author)
        self.price = self.val_price(price)

    @staticmethod
    def val_count(pages_count):
        if pages_count < 300:
            return pages_count
        raise PageCountError

    @staticmethod
    def val_year(correct_year):
        if correct_year > 2005:
            return correct_year
        raise YearError

    @staticmethod
    def val_author(author_name: str):
        if isinstance(author_name, str):
            return author_name
        raise AuthorError

    @staticmethod
    def val_price(book_price):
        max_price = 3000
        if book_price < max_price:
            return book_price
        raise PriceError(book_price, max_price)


myBook = Book(150, 2007, "dsfsdfs", 1600)
