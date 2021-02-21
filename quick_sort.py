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


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1


p = 0
r = len(A)
quick_sort(A, p, r)

print("quick sorted list: ", A)










