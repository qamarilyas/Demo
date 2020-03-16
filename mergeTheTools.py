def merge_the_tools(string, k):

    for i in range(0,len(string),k): # iterate over i with index 0 to avery k
        s = ""
        for j in string[i:i+k]: # iterate over each k characters
            if j not in s:
                s+=j
        print(s)

string, k = input(), int(input())
merge_the_tools(string, k)