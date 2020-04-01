
'''

n = int(input()) # number of elements in the set
s = set(map(int, input().split())) # elements of the sets space sepeerated stored in s

N=int(input()) # number of commands to execute
for i in range(N):
    method, *args = input().split()+[''] # stores coomand in method and value in method and args [''] is added so
    # pop is also covered and does not give an error
    eval('s.{0}({1})'.format(method,*args)) # s.discard(6) will be executed.

print(sum(s))

'''
# The above code works fine but it takes commands which are not valid. Should only accept commands from these 3.
# we can extend above code for this purpose.

n = int(input()) # number of elements in the set
s = set(map(int, input().split())) # elements of the sets space sepeerated stored in s

methods = {
    'pop': 'pop',
    'remove': 'remove',
    'discard': 'discard'

}
N=int(input()) # number of commands to execute
for i in range(N):
    method, *args = input().split()+[''] # stores coomand in method and value in method and args [''] is added so
    # pop is also covered and does not give an error
    eval('s.{0}({1})'.format(methods[method],*args)) # s.discard(6) will be executed.

print(sum(s))

'''
methods = {
    'pop' : s.pop,
    'remove' : s.remove,
    'discard' : s.discard
}

for _ in range(N):
    method,*args=input().split()
    methods[method](*map(int, args))

print(sum(list(s)))

'''