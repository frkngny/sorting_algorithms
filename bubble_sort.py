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


def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                key = A[j]
                A[j] = A[j-1]
                A[j-1] = key


bubble_sort(A)
print("bubble sorted list: ", A)











