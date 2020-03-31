from itertools import combinations_with_replacement

a,b= input().split()

#for x in range(int(b)):

for i in combinations_with_replacement(sorted(a),int(b)):
    #print (list(permutations(a,int(b))))
    print(''.join(i).upper())
