

class BankAccount:

    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance

data_list = input().split(' | ')

accounts_list = []

while not data_list[0] == 'end':
    bank = data_list[0]
    name = data_list[1]
    balance = float(data_list[2])
    bank_account = BankAccount(name, bank, balance)
    accounts_list.append(bank_account)
    data_list = input().split(' | ')

#print all Accounts, ordered by their balance, in descending order, and then by length of the bank name, in ascending order.
#minusa znachi descending
for account in sorted(accounts_list, key=lambda acc: (-acc.balance, len(acc.bank))):
    print(f'{account.name} -> {account.balance:.2f} ({account.bank})')


