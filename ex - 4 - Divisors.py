NUM = input("please enter a number ")

for x in range(1, 100):
    if int(NUM) % x == 0:
        print(x)
