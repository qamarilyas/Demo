from itertools import combinations

n,l,k=input(),input().split(),int(input())

i=list(combinations(l,k))
t=[x for x in i if 'a' in x]

print(len(t)/len(i))

