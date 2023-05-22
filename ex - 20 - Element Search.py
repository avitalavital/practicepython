STR = input("enter a list of numbers with spase betwin the numbers ")
LIST = STR.split(" ")
print(LIST)

NUM = input("enter a number ")


def func(NUM, LIST):
    return NUM in LIST


print(func(NUM, LIST))
