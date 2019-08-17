class Book:
    def __init__(self, title, author:str, price:float):
        self.title = title
        self.author = author
        self.price = price

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        first_name, second_name = value.split()
        for chrx in second_name:
            if chrx.isdigit():
                raise Exception('Author not valid!')
            break
        self.__author = value

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
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise Exception('Price not valid!')
        else:
            self.__price = value

    def __str__(self):
        return f'Type: Book\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}'


class GoldenEditionBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author, price)
        self.price = 1.3 * price

    def __str__(self):
        return f'Type: GoldenEditionBook\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}'

book1 = Book('koss', 'Inva andonov', 12.4444)

print(book1)
book2 = GoldenEditionBook('koss', 'ivan asds', 12.4444)
print(book2)