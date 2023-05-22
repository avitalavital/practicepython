A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
B = []
NUM = input("enter a number")
for x in A:
    if x < int(NUM):
        print(x)
        B.append(x)
print(B)
