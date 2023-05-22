num = input("enter a number ")

if int(num) % 2 == 1:
    print("the number is odd")
elif int(num) % 2 == 0:
    print("the number is even")

num4 = input("enter another a number ")
if int(num4) % 4 == 0:
    print("the number is a multiple of 4")
else:
    print("the number isn't a multiple of 4")

check = input("enter number to check ")
divide = input("enter number to divide by ")

if int(check) % int(divide) == 0:
    print(check + " divides evenly by" + divide)
else:
    print(check + " doesn't divide evenly by " + divide)
