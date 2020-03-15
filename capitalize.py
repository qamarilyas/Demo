import string

alpha=string.ascii_lowercase

n=int(input())
width=4*n-3
L=[]
for i in range(n):

    ch= "-".join(alpha[i:n])
    L.append((ch[::-1]+ch[1:]).center(width, "-"))
print("\n".join(L[::-1]+L[1:]))