##optimized banking system


class BankAccount:
    def __init__(self, name:str, bank:str, balance:str):
        self.name = name
        self.bank = bank
        self.balance = balance

    def sort_data(self):
        pass

    def __str__(self):
        return f'{self.name} -> {self.balance} ({self.bank})'


def collect_data():
    user_input = input().split(' | ')
    data_list = []
    while user_input[0] != 'end':
        bank = user_input[0]
        name = user_input[1]
        balance = user_input[2]
        account = BankAccount(name, bank, balance)
        data_list.append(account)
        user_input = input().split(' | ')
    return data_list

data_list= collect_data()
for item in data_list:
    print(item)
