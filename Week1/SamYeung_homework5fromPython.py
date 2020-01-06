#HW5
#List

numberList = []
while True:
    userInput = input('Please enter a number (RETURN/ENTER when done): ')
    if userInput == '':
        break
    numberList.append(float(userInput))

print('The numbers entered were:')
print(numberList)

minimumValue = numberList[0]
maximumValue = numberList[0]
total = 0

for number in numberList:
    if number < minimumValue:
        minimumValue = number
    elif number > maximumValue:
        maximumValue = number
    total += number

averageValue = total / len(numberList)
print('Minimum value was:', minimumValue)
print('maximumValue value was:', maximumValue)
print('The sum is:', total)
print('Average value was:', averageValue)
