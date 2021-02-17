import random

index = int(input("index: "))

lower = int(input("lower bound: "))
upper = int(input("upper bound: "))


A = list()
for ind in range(index):

    value = random.randint(lower, upper)
    A.append(value)

org_list = A.copy()
for j in range(1, len(A)):
    key = A[j]

    i = j-1
    while i > -1 and A[i] > key:
        A[i+1] = A[i]
        i = i-1

    A[i+1] = key


print("original list: ", org_list)
print("sorted list: ", A)



