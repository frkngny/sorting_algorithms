import random
import math

index = int(input("index: "))

lower = int(input("lower bound: "))
upper = int(input("upper bound: "))

random.seed(1)
A = list()
for ind in range(index):

    value = random.randint(lower, upper)
    A.append(value)

org_list = A.copy()
print('original list: ', org_list)

r = len(A) - 1


def merge(A, p, q, r):
    n1 = q-p+1
    n2 = r-q

    L = [0] * n1
    R = [0] * n2
    L.append(999999999)
    R.append(999999999)

    for i in range(n1):
        L[i] = A[p+i]

    for j in range(n2):
        R[j] = A[q+j+1]

    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    if len(A) == (n1+n2):
        print("merge sorted list: ", A)


def merge_sort(A, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


merge_sort(A, 0, r)
