import math
ab=int(input())
bc=int(input())

x=round(math.degrees(math.atan2(ab,bc)))  #calculate the theta  using atan2 and degree
print(x)

#print(str(int(c*180/cmath.pi))+'°')
