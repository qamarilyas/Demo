A=set(input().split())
n= int(input())
for _ in range(n):
    if not A.issuperset(set(input().split())):
        print ("False")
        break
else:
    print("True")

