e=int(input())
A=set(map(int,input().split()))

f=int(input())

#b=set(map(int,input().split()))
methods = {
    'intersection_update': 'intersection_update',
    'update':'update',
    'symmetric_difference_update':'symmetric_difference_update',
    'difference_update':'difference_update'



}

for i in range(f):
    method,b=input().split()
    c=set(map(int,input().split()))
    eval('A.{0}({1})'.format(methods[method], c))

print(sum(A))