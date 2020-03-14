
def doorMat(rows,colmns):
    #upper triangle
    for i in range(0,int(rows/2)):
        pattern= '-|-'*((2*i)+1)
        print(pattern.center(colmns,"-"))

    #Center
    print("WELCOME".center(colmns,"-"))

    #Lower triangle
    i=int(rows/2)-1
    while(i>=0):
        pattern = '-|-' * ((2 * i) + 1)
        print(pattern.center(colmns, "-"))
        i-=1

# We will devide the problem in 3 parts. upper triangle, center and lower triangle

rows,colmns= map(int,input().split())
doorMat(rows,colmns)