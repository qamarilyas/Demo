
def bubbleSort(lst):
    for i in range(len(lst)-1): # outer loop run from index 0 to len(lst)
        for j in range((len(lst)-i)-1): # inner loop run from index 0 to omitting i values
            if(lst[j]>lst[j+1]):
                lst[j],lst[j+1]=lst[j+1],lst[j] # swap each time if second value is greater
    print(lst)




lst=[5,7,3,11,9,2]
bubbleSort(lst)