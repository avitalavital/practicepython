A = input("enter your first  num ")
B = input("enter your second  num ")
C = input("enter your third  num ")
LST = [A, B, C]
print(LST)

# if A>B and A>C:
#    print(a + " " + "is the biggest")
# elif B>A and B>C:
#    print(b + " " + "is the biggest")
# elif C>A and C>B:
#    print(c + " " + "is the biggest")
# else:
#    print("no number is the biggest")

if A == max(LST):
    print(A + " " + "is the biggest")
elif B == max(LST):
    print(B + " " + "is the biggest")
elif C == max(LST):
    print(C + " " + "is the biggest")
