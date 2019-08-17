## 06 Animals


class Dog:
    def __init__(self, name, age, number_of_legs):
        self.name = name
        self.age = age
        self.number_of_legs = number_of_legs

    def produce_sound(self):
        return f'Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.number_of_legs}'


class Cat:
    def __init__(self, name, age, intelligence_quotient):
        self.name = name
        self.age = age
        self.intelligence_quotient = intelligence_quotient


    def produce_sound(self):
        return f'Cat: {self.name}, Age: {self.age}, IQ: {self.intelligence_quotient}'


class Snake:
    def __init__(self, name, age, cruelty_coefficient):
        self.name = name
        self.age = age
        self.cruelty_coefficient = cruelty_coefficient

    def produce_sound(self):
        return f'Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruelty_coefficient}'


user_input = input()
dogs = []
cats = []
snakes = []
temp_list = []
who_is_talking = []

while user_input != 'I\'m your Huckleberry':
    temp_list = []
    current_input = user_input.split()
    if current_input[0] == 'talk':
        who_is_talking.append(current_input[1])
    elif current_input[0] == 'Dog':
        name = current_input[1]
        temp_list.append(name)
        age = current_input[2]
        temp_list.append(int(age))
        number_of_legs = current_input[3]
        temp_list.append(int(number_of_legs))
        dogs.append(temp_list)

    elif current_input[0] == 'Cat':
        name = current_input[1]
        temp_list.append(name)
        age = current_input[2]
        temp_list.append(int(age))
        intelligence_quotient = current_input[3]
        temp_list.append(int(intelligence_quotient))
        cats.append(temp_list)

    elif current_input[0] == 'Snake':
        name = current_input[1]
        temp_list.append(name)
        age = current_input[2]
        temp_list.append(int(age))
        cruelty_coefficient = current_input[3]
        temp_list.append(int(cruelty_coefficient))
        snakes.append(temp_list)

    user_input = input()

for item in who_is_talking:
    for element in dogs:
        if item == element[0]:
            print(f'I\'m a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.')

    for element in cats:
        if item == element[0]:
            print(f'I\'m an Aristocat, and I will now produce an aristocratic sound! Myau Myau.')

    for element in snakes:
        if item == element[0]:
            print(f'I\'m a Sophistisnake, and I will now produce a sophisticated sound! Honey, I\'m home.')


for element in dogs:
    print(Dog(element[0], element[1], element[2]).produce_sound())
for element in cats:
    print(Cat(element[0], element[1], element[2]).produce_sound())
for element in snakes:
    print(Snake(element[0], element[1], element[2]).produce_sound())
