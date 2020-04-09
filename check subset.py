t=int(input())

for i in range(t):
    s1=int(input())
    A=set(map(int,input().split()))
    s2 = int(input())
    B = set(map(int, input().split()))
    x=B.issubset(A)
    print(x)