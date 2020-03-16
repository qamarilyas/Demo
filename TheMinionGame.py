def minion_game(string):
    # your code goes here
    Stuart=0
    Kevin=0
    vowel='AEIOU'
    for i in range(len(string)):
        if(string[i].upper() in vowel):
            Kevin=Kevin+len(string)-i
        else:
            Stuart=Stuart+len(string)-i
    if(Kevin>Stuart):
        print("{} {}".format('Kevin', Kevin))
    elif (Kevin < Stuart):
        print("{} {}".format('Stuart', Stuart))
    elif(Kevin==Stuart):
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)