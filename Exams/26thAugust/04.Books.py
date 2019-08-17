
####probvai bez class da go pravish ...

class Books:
    def __init__(self, title, author, price:float, chapters:[]):
        self.title = title
        self.author = author
        self.price = price
        self.chapters = chapters

    def __str__(self):
        return f'SOLD: {title} with author {author}. Chapters in the book {sum([chapters.count(item) for item in chapters])}'

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            raise Exception('Invalid price!')


user_input = input()
books = {}
v = 0
while True:
    if user_input == 'on work':
        break
    try:
        data = user_input.split('->')
        title, author, price = data[0].split()
        price = float(price)
        chapters= data[1].split(', ')
        book = Books(title=title, author=author, price=price, chapters=chapters)
        v += 1
        books[f'Book{str(v)}'] = book
    except:
        pass
    user_input = input()

price = 0

while True:
    title_to_find = input()
    if title_to_find == 'end work':
        break
    for k,v in books.items():
        if v.title == title_to_find:
            print(v)
            price += float(v.price)
        else:
            print('No such book here')

print(f'Money: {price:.2f}')
