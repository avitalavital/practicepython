import datetime

date = datetime.datetime.now()
name = input("enter your name ")
age = input("enter your age ")
repeat = input("enter times to repeat ")


def before(b):
    return date.year + (100 - int(age))


def after(a):
    return date.year - (int(age) - 100)


if int(age) < 100:
    print(f"{name} you will be 100 years old in {before(age)} \n" * int(repeat))
    # print((name + ", you will be 100 years old in " + (str(before(age))) + "\n") * int(repeat))
else:
    print(f"{name} you were 100 years old at {after(age)} \n" * int(repeat))
    # print((name + ", you were 100 years old at " + (str(after(age))) + "\n") * int(repeat))
