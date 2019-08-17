
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

#print class type automatically as variable works for parent class

    def __str__(self):
        return f'Type: {self.__class__.__name__}\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}'

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if len(value) < 3:
            raise Exception('Title not valid!')
        else:
            self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        item_list = value.split()
        for item in item_list:
            for letter in item:
                if letter.isdigit():
                    raise Exception('Author not valid!')
        else:
            self.__author = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception('Price not valid!')
        else:
            self.__price = value


class GoldenEditionBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author, price)
        self.price = price * 1.3


author = input()
title = input()
price = float(input())

try:
    book1 = Book(title=title, author=author, price=price)
    book2 = GoldenEditionBook(title=title, author=author, price=price)
    print(book1)
    print()
    print(book2)
except Exception as ex:
    print(ex)
