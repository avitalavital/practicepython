name = input("enter your name ")
age = input("enter your age ")
repeat = input("enter times to repeat ")


def before(age):
    return 2023 + (100 - int(age))


def after(age):
    return 2023 - (int(age) - 100)


if int(age) < 100:
    print((name + ", you will be 100 years old in " + (str(before(age))) + "\n") * int(repeat))
else:
    print((name + ", you were 100 years old at " + (str(after(age))) + "\n") * int(repeat))

# i=0
# while i < int(repeat):
#    print ((name) + ", you will be 100 years old in " + (str(wb(age))))
#    i += 1
