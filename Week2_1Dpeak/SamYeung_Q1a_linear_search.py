'''
Man Yeung (Sam)
Week2_find a peak
'''

def FindAPeak(L):    
    if not L:
        return "List is empty"
    
    i = 0
    while True:
        if i == len(L)-1:
            return L[i]
        elif L[i] < L[i+1]:
            i += 1
        else:
            return L[i]

if __name__ == "__main__":
    test = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    numberList = [15,20,18,6,0,0,21,22,24]

    testZero = []
    testOne = [1]

    print("original:", test)
    print("Find A peak:", FindAPeak(test))
    print()
    print("original:", numberList)
    print("Find A peak2:", FindAPeak(numberList))
    print()
    print("original:", testZero)
    print("Find A peak3:", FindAPeak(testZero))
    print()
    print("original:", testOne)
    print("Find A peak4:", FindAPeak(testOne))


#total time ~ O(n log n)
#total space ~ C
