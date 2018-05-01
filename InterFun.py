## Name:  Michael Martin
## Date:  4.30.2018
## Desc:  Assignment for Intersection Function:

##
##    With the given input: a = [ 1, 4, 5, 7,8 12] and b = [4, 5 , 9 ,12, 15, 2 ]
##    create an intersection function:
##    c = intersect(a,b)
##    where c is the set that contains the intersection of sets a and b.
##    You program is to output the result of the intersection function

# # # # # #


def intersect():

    a = [1, 4, 5, 7, 8, 12]
    b = [4, 5 , 9 ,12, 15, 2]
    preC = a + b
    ## print(preC)
    c = []
    count = 0
    aList = []
    bList = []
    cList = []

    
    for letter in a:
        if letter in b:
            aList.append(letter)
        elif letter in b:
            bList.append(letter)
        else:
            cList.append(letter)

    print(aList)
    print(bList)
    print(cList)


    ##


def main():

    intersect()
    



main()







    


