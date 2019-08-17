import re

class Mankind:
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


class Student(Mankind):
    def __init__(self, first_name, last_name, faculty_number):
        Mankind.__init__(self, first_name, last_name)
        self.faculty_number = faculty_number

    def __str__(self):
        return f'First Name: {self.first_name}\nLast Name: {self.last_name}\nFaculty number: {self.faculty_number}\n'

    @property
    def faculty_number(self):
        return self.__faculty_number

    @faculty_number.setter
    def faculty_number(self, value):
        regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')
        if 5 <= len(str(value)) <= 10 and regex.search(value) is None:
            self.__faculty_number = value
        else:
            raise Exception("Invalid faculty number!")


class Worker(Mankind):
    def __init__(self, first_name, last_name, week_salary:float, working_hours:float):
        Mankind.__init__(self, first_name, last_name)
        self.week_salary = float(week_salary)
        self.working_hours = float(working_hours)

    def money_per_hr(self):
        payment_per_hour = self.week_salary / (self.working_hours * 5)
        return payment_per_hour

    def __str__(self):
        return f'First Name: {self.first_name}\nLast Name: {self.last_name}\nWeek Salary: ' \
            f'{self.week_salary:.2f}\nHours per day: {self.working_hours:.2f}\nSalary per hour: {self.money_per_hr():.2f}'

    @property
    def week_salary(self):
        return self.__week_salary

    @week_salary.setter
    def week_salary(self, value):
        if float(value) > 10:
            self.__week_salary = value
        else:
            raise Exception("Expected value mismatch! Argument: weekSalary")
    
    @property
    def working_hours(self):
        return self.__working_hours
    
    @working_hours.setter
    def working_hours(self, value):
        if value >= 1 and value <= 12:
            self.__working_hours = float(value)
        else:
            raise Exception("Expected value mismatch! Argument: workHoursPerDay")


user_input1 = input().split()
user_input2 = input().split()


try:
    student = Student(first_name=user_input1[0], last_name=user_input1[1], faculty_number=str(user_input1[2]))
    worker = Worker(first_name=user_input2[0], last_name=user_input2[1], week_salary=float(user_input2[2]),
                    working_hours=float(user_input2[3]))
    print(student)
    print(worker)
except Exception as ex:
    print(ex)
