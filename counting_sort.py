import random

index = int(input("index: "))

lower = int(input("lower bound: "))
upper = int(input("upper bound: "))

random.seed(1)
A = list()
for ind in range(index):

    value = random.randint(lower, upper)
    A.append(value)


print("original list: ", A)


def counting_sort(A):
    k = 0
    for i in range(len(A)):
        if A[i] > k:
            k = A[i]

    B = list(A)
    C = list()
    for i in range(k):
        C.append(0)

    for j in range(0, len(A)):
        C[A[j]-1] += 1

    for i in range(1, k):
        C[i] += C[i-1]

    for j in range(len(A)-1, -1, -1):
        B[C[A[j]-1]-1] = A[j]
        C[A[j]-1] -= 1

    return B


ret = counting_sort(A)
print('counting sorted list: ', ret)

