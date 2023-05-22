nnaci = input("how many Fibonnaci numbers to generate? ")
a = [1, 1]


def fibo(nnaci):
    for i in range(int(nnaci) - 2):
        a.append(a[-2] + a[-1])
    return a


print(fibo(nnaci))
