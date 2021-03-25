import random

index = int(input("index: "))

random.seed(1)
A = list()
for ind in range(index):

    value = random.random()
    A.append(value)


def insertion_sort(C):
    for j in range(1, len(C)):
        key = C[j]

        i = j - 1
        while i > -1 and C[i] > key:
            C[i + 1] = C[i]
            i = i - 1

        C[i + 1] = key
    return C


def bucket_sort(A):
    B = []
    n = len(A)

    for i in range(n):
        B.append([])

    for i in range(1, n+1):
        val = int(n * A[i - 1])
        B[val].append(A[i-1])

    for i in range(n):
        B[i] = insertion_sort(B[i])

    print(B)


bucket_sort(A)
