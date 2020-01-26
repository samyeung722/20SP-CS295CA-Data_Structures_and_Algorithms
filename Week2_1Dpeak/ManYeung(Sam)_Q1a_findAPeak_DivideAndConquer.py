'''
Man Yeung (Sam)
Week2_find a peak
'''

def FindAPeak(L):    
    if not L:
        return "List is empty"

    mid = len(L)//2
    print('mid index:', mid)
    
    while True:
        if mid <= 0 or mid >= len(L) or (L[mid - 1] <= L[mid] and L[mid + 1] <= L[mid]):
            return L[mid]
        elif L[mid - 1] >= L[mid]:
            mid = mid - mid // 2
        elif L[mid + 1] >= L[mid]:
            mid = mid + mid // 2

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
