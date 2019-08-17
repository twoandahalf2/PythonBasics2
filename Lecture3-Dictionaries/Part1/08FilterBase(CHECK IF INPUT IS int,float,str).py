class FilterBase:

    age_dict = {}
    salary_dict = {}
    gender_dict = {}


    def logic_while(self):
        user_input = input().split(' -> ')
        while user_input[0] != 'exit':
            try:
                value = int(user_input[1])
                self.age_dict[user_input[0]] = value
            except ValueError:
                try:
                    value = float(user_input[1])
                    self.salary_dict[user_input[0]] = value
                except ValueError:
                    value = user_input[1]
                    self.position_dict[user_input[0]] = value
            user_input = input().split(' -> ')

    def print_all(self):
        what_are_we_printing = input()
        if what_are_we_printing == 'Position':
            for key,value in self.position_dict.items():
                print(f'Name: {key}')
                print(f'Position: {value}')
                print('====================')
        elif what_are_we_printing == 'Age':
            for key,value in self.age_dict.items():
                print(f'Name: {key}')
                print(f'Age: {value}')
                print('====================')
        elif what_are_we_printing == 'Salary':
            for key,value in self.salary_dict.items():
                print(f'Name: {key}')
                print(f'Salary: {value}')
                print('====================')


if __name__ == '__main__':
    FilterBase().logic_while()
    FilterBase().print_all()

