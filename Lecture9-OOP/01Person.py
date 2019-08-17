class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = self.validate_age(age)

    # for the getter and setter we use:
    #		self.age = age

    def validate_age(self, age):
        if age > 0:
            return age
        else:
            raise Exception("Age must be positive!")

    def validate_name(self, name):
        if len(name) < 3:
            print('Name\'s length should not be less than 3 symbols!')
        else:
            return name


# #getter and setter are used for validation or alternatively
# #with the function - validate_age
# @property
# def age(self):
# 	return self.__age
#
# @age.setter
# def age(self,value):
# 	if value < 0:
# 		raise Exception("Age must be positive!")
# 	else:
# 		self.__age = value

class Child(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)
        self.age = self.validate_age2(age)

    def validate_age2(self, age):
        if age < 15:
            return age
        else:
            raise Exception("Child's age must be less than 15!")

    def __str__(self):
        return f'Name: {self.name}, Age:{self.age}'


user_input = input()
name,age = user_input.split()