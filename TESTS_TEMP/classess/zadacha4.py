#Exercises


class Exercises:
    def __init__(self, topic:str, course_name:str, judge_contest_link:str, problems:[]):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems

    def __str__(self):
        return f'Exercises: {self.topic}\nProblems for exercises and homework for the ' \
            f'"{self.course_name}" course @ SoftUni.' \
            f'\nCheck your solutions here: {self.judge_contest_link}\n'

exercise_1 = Exercises('ObjectsAndSimpleClasses', 'ProgrammingFundamentalsExtended',
                       'https://judge.softuni.bg/Contests/439', ['Exercises', 'OptimizedBankingSystem'])

print(exercise_1, end='')
counter = 1
for item in exercise_1.problems:
    print(f'{counter}. {item}')
    counter += 1