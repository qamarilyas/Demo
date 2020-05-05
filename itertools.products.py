from itertools import product

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

for i in product(A, B):
    print(i, end=" ")
