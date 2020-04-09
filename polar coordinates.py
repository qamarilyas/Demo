from cmath import polar,phase

#Two ways to solve this

y=complex(input()) #input

#solution 1
x=polar(y)
print(x[0])
print(x[1])

#solution 2
print(abs(y))
print(phase(y))




