'''
Sam Yeung

Week1 in class question 1 and 2

find the max and next max in an array of integers

list len bug free
'''

numberList = [15,20,18,6,25,19,-1,-20]

#numberList = [15] #check for bug in case list has only one number

print('The numbers are:')
print(numberList)

maximumValue = numberList[0]    #T:C, S:C
secondMaximumValue = None  #T:C, S:C

for number in numberList:   #T:nC, S:0
    if number > maximumValue:   #T:nC*C, S:0
        secondMaximumValue = maximumValue #T:nC*C*C, S:0
        maximumValue = number   #T:nC*C*C*C, S:0
        
print('Maximum Value is:', maximumValue)
print('Second Maximum Value is:', secondMaximumValue)

#total time ~ nC
#total space = 2C = C
