#07 Websites:


class Websites:
    def __init__(self, host, domain, queries=''):
        self.host = host
        self.domain = domain
        self.queries = queries

    def show_output(self):
        if self.queries == '':
            return f'https://www.{self.host}.{self.domain}'
        else:
            my_list = self.queries.split(',')
            v = f'/query?=[{"]&[".join(my_list[0:])}]'
            return f'https://www.{self.host}.{self.domain}{v}'


def main():
    user_input = input()
    counter = 0
    while user_input != 'end':
        data = user_input.split(' | ')
        host = data[0]
        domain = data[1]
        for item in data:
            counter += 1
        if counter > 2:
            queries = data[2]
            print(Websites(host, domain, queries).show_output())
        else:
            print(Websites(host, domain).show_output())
        counter = 0
        user_input = input()


if __name__ == '__main__':
    main()