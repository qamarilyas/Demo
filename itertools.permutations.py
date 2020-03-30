from itertools import permutations

#print(list(permutations(['1','2','3'])))

a,b=input().split()

for i in permutations(sorted(a),int(b)):
    #print (list(permutations(a,int(b))))
    print(''.join(i).upper())
