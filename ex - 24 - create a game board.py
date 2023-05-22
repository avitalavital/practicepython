def line(num):
    print("--- "*num)
def column(num):
    print("|   "*num + "|")

num = int(input("enter game board size "))

for i in range(num):
    line(num)
    column(num)
line(num)