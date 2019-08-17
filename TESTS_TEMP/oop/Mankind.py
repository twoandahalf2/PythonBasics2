class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        for i in value:
            if i.isupper():
                pass
            else:
                raise Exception('Expected upper case letter! Argument: firstName')
            break
        if len(value) <= 3:
            raise Exception('Expected length at least 4 symbols! Argument: firstName')
        else:
            self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        for i in value:
            if i.isupper():
                pass
            else:
                raise Exception('Expected upper case letter! Argument: lastName')
            break
        if len(value) <= 2:
            raise Exception('Expected length at least 3 symbols! Argument: lastName')
        else:
            self.__last_name = value


class Worker(Human):
    def __init__(self, first_name, last_name, week_salary:int, work_hours_per_day:int):
        Human.__init__(self,first_name, last_name)
        self.week_salary = week_salary
        self.work_hours_per_day = work_hours_per_day

    def calculate_salary_per_hour(self):
        salary_per_hour = self.week_salary / 5 / self.work_hours_per_day
        return salary_per_hour

    def __str__(self):
        return f'First Name:{self.first_name}\nLast Name:{self.last_name}\nWeek Salary:{self.week_salary:.2f}' \
               f'\nHours per day:{self.work_hours_per_day:.2f}\nSalary per hour: {self.calculate_salary_per_hour():.2f}'

    @property
    def week_salary(self):
        return self.__week_salary

    @week_salary.setter
    def week_salary(self, value):
        if int(value) <= 10:
            raise Exception('Expected value mismatch! Argument: weekSalary')
        else:
            self.__week_salary = int(value)

    @property
    def work_hours_per_day(self):
        return self.__work_hours_per_day

    @work_hours_per_day.setter
    def work_hours_per_day(self, value):
        if 1 < int(value) < 12:
            self.__work_hours_per_day = int(value)
        else:
            raise Exception('Expected value mismatch! Argument: workHoursPerDay')


class Student(Human):
    def __init__(self, first_name, last_name, faculty_number):
        Human.__init__(self,first_name, last_name)
        self.faculty_number = faculty_number

    def __str__(self):
        return f'First Name:{self.first_name}\nLast Name:{self.last_name}\nFaculty Number:{self.faculty_number}'

    @property
    def faculty_number(self):
        return self.__faculty_number

    @faculty_number.setter
    def faculty_number(self, value):
        if 5 < len(value) < 10:
            self.__faculty_number = value
        else:
            raise Exception('Invalid faculty number!')


try:
    student = input().split()
    worker = input().split()
    student1 = Student(student[0], student[1], student[2])
    worker1 = Worker(worker[0], worker[1], int(worker[2]), int(worker[3]))
    print(student1)
    print()
    print(worker1)
except Exception as f:
    print(f)


