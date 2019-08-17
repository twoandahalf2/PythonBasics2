class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if len(value) > 2:
            self.__last_name = value
        else:
            raise Exception("Last name: more than 2 symbs needed")
        for letter in value:
            if letter == letter.upper():
                self.__last_name = value
                break
            else:
                raise Exception('Last name: has to start with upper case')

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
                raise Exception('First name: has to start with upper case')

    @first_name.setter
    def first_name(self,value):
        if len(value) > 2:
            self.__first_name = value
        else:
            raise Exception("First name: more than 2 symbs needed")




Jack = Person('Ja', 'sparrow')
print(Jack.first_name)
print(Jack.last_name)
