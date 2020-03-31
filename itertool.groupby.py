from itertools import groupby

x=input()

#print(list(groupby(x)))

for a,b in groupby(x):
    print(*[(len(list(b)),int(a))],end="")