def selectionSort(lst):
    minindex=0
    for i in range(len(lst)-1): # outer loop run from index 0 to len(lst)
        for j in range(i, len(lst)-1): # inner loop run from index i to len(lst) saving min at index j
            if(lst[j+1]>lst[j]):
                minindex=j
                #lst[j],lst[j+1]=lst[j+1],lst[j] # swap each time if second value is greater
            lst[j],lst[minindex]=lst[minindex],lst[j]
    print(lst)




lst=[5,7,3,11,9,2]
selectionSort(lst)