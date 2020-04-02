k=input()
x=list(map(int,input().split()))

a={}

for i in x:
    if i in a:
        a[i]+=1
    else:
        a[i]=1

for j in a:
    if a[j]==1:
        print(j)
        break
