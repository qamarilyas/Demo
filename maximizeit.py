from itertools import product
k, m = map(int, input().split())

n = (list(map(int, input().split()))[1:] for i in range(k))
results = (sum(num ** 2 for num in numbers) % m for numbers in product(*n))
print(max(results))




'''

k,m=map(int,input().split())

max = 0
total=0
#print(type(max))
for i in range(k):
    l=input().split()
    for x in range(1,len(l)):
        #max = math.max(int(l[x]))
        if(int(l[x])>int(max)):
            max=int(l[x])

    #print(type(max))
    total+=max ** 2
print(total%m)

'''