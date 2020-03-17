A=set(input().split()) # Set A defined
n= int(input()) # Len of the input of subsets
for _ in range(n):
    if not A.issuperset(set(input().split())): # VERIFY that A is not superset of any of it
        print ("False")
        break
else: # True if A is superset of all
    print("True")

