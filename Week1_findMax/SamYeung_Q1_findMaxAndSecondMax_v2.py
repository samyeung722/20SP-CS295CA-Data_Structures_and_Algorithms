'''
Sam Yeung
find the max and next max in an array of integers
'''

numberList = [15,20,18,6,25,19,-1,21,22,24]

print('The numbers entered were:')
print(numberList)

maximumValue = 0 #T:C, S:C
secondMaximumValue = 0 #T:C, S:C

if numberList[0] > numberList[1]:   #T:C, S:C
    maximumValue = numberList[0]    #T:C, S:C
    secondMaximumValue = numberList[1]  #T:C, S:C
else:
    maximumValue = numberList[1]    #T:C, S:C
    secondMaximumValue = numberList[0]  #T:C, S:C

for number in range(2,len(numberList)):   #T:nC, S:0
    if numberList[number] > maximumValue:   #T:nC*C, S:0
        secondMaximumValue = maximumValue #T:nC*C*C, S:0
        maximumValue = numberList[number]   #T:nC*C*C, S:0
    elif numberList[number] > secondMaximumValue: #T:nC*C, S:0
        secondMaximumValue = numberList[number] #T:nC*C*C, S:0
        
print('Maximum Value is:', maximumValue)
print('Second Maximum Value is:', secondMaximumValue)


#total time ~ nC
#total space = 2C = C
