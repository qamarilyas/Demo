from itertools import combinations

#print(list(permutations(['1','2','3'])))

a,b=input().split()

for x in range(int(b)):

    for i in combinations(sorted(a),x+1):
    #print (list(permutations(a,int(b))))
        print(''.join(i).upper())
