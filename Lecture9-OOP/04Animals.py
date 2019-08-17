class Animal:
    def __init__(self, name, age:int, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'{self.__class__.__name__}\n{self.name} {self.age} {self.gender}\n{self.produce_sound()}\n'

    def produce_sound(self):
        pass

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if int(value) <= 0:
            raise Exception('Invalid input!')
        else:
            self.__age = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value == 'Male' or value == 'Female':
            self.__gender = value
        else:
            raise Exception('Invalid input!')


class Dog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name,age,gender)

    def produce_sound(self):
        return f'Woof!'


class Frog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name,age,gender)

    def produce_sound(self):
        return f'Ribbit'


class Cat(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name,age,gender)

    def produce_sound(self):
        return f'Meow meow'


class Kitten(Cat):
    def __init__(self, name, age, gender='female'):
        Cat.__init__(self, name, age, gender)
        self.gender = 'Female'

    def produce_sound(self):
        return f'Meow'


class Tomcat(Cat):
    def __init__(self, name, age, gender='male'):
        Cat.__init__(self, name,age,gender)
        self.gender = 'Male'

    def produce_sound(self):
        return f'MEOW'

animals_list = []

while True:
    class_type = input()
    user_input = input().split()
    if class_type == 'Beast!':
        break
    if class_type != 'Dog' and class_type != 'Frog' and class_type != 'Cat' and class_type != 'Kitten' and\
            class_type != 'Tomcat':
        print('Invalid input!')
        continue
    name = user_input[0]
    age = user_input[1]
    gender = user_input[2]
    obj_str = f"{class_type}(\"{name}\",{int(age)},\"{gender}\")" ### Get a class type from variable
    try:
        obj = eval(obj_str)
        animals_list.append(obj)
    except Exception as ex:
        print(ex)

for a in animals_list:
    print(a)

