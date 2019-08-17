
compare_type = input()


def compare_int():
    a = int(input())
    b = int(input())
    if a > b:
        print(a)
    else:
        print(b)

def compare_char():
    a = input()
    b = input()
    if ord(a) > ord(b):
        print(a)
    else:
        print(b)

def compare_string():
    a = input()
    b = input()
    if len(a) > len(b):
        print(a)
    else:
        print(b)


if __name__ == '__main__':
    if compare_type == 'int':
        compare_int()
    elif compare_type == 'char':
        compare_char()
    else:
        compare_string()

