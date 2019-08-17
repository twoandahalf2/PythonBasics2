class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise Exception('age must be positive')
        else:
            self.__age = value


class Child(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 15:
            raise Exception('age must be lower than 15')
        else:
            self.__age = value


person1 = Person('Vladi', -1)
child1 = Child('Qna', 16)
print(person1.age)
print(child1.age)