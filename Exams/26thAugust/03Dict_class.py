class Person:
    def __init__(self, first_name , last_name, age, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birthdate = birthdate

    def __str__(self):
        return f'Name of the person: {first_name} {last_name}\nAge of the person: {age}.\n' \
            f'Birthdate of the person: {birthdate}'

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if len(value) > 2:
            self.__last_name = value
        else:
            raise Exception("Expected length at least 3 symbols! Argument: lastName")
        for letter in value:
            if letter == letter.upper():
                self.__last_name = value
                break
            else:
                raise Exception('Expected upper case letter! Argument: lastName')

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        for letter in value:
            if letter == letter.upper():
                self.__first_name = value
                break
            else:
                raise Exception('Expected upper case letter! Argument: firstName')
        if len(value) > 3:
            self.__first_name = value
        else:
            raise Exception("Expected length at least 4 symbols! Argument: firstName")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 9 < value < 100:
            self.__age = value

    @property
    def birthdate(self):
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, value):
        date = value.split('-')
        if len(date) == 3:
            self.__birthdate = value


user_input = input()
result = []

while True:
    user_input=user_input.split()
    if user_input[0] == 'make':
        break
    else:
        pass
    try:
        first_name = user_input[4]
        last_name = user_input[5]
        age = int(user_input[8])
        birthdate = user_input[14]
        person = Person(first_name=first_name, last_name=last_name, age=age, birthdate=birthdate)
        print(person)
    except:
        pass
    user_input = input()

if not result:
    print('DB is empty')
