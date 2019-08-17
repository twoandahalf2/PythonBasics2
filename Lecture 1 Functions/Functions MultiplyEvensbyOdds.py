




class Zadacha():
    my_number = input()


    def calculate(self):

        sum_even = 0
        sum_odd = 0
        for i in self.my_number:
            if i == '-':
                continue
            i = int(i)
            if i % 2 == 0:
                sum_even += i
            if i % 2 != 0:
                sum_odd += i
        return [sum_even, sum_odd]


    def multiple(self):
        n = Zadacha().calculate()
        x, y = n
        result = x * y
        return result



if __name__ == '__main__':
    print(Zadacha().multiple())

