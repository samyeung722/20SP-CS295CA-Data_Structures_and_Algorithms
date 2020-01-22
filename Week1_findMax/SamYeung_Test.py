#HW6
#Strings

def countCharInString (findChar , targetString):
    return targetString.count(findChar)

phrase = input('Please enter a phrase: ')
phrase = phrase.lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
letterCountZeroList = []

for letter in alphabet:
    count = countCharInString(letter, phrase)
    if count == 1:
        print('There is only 1', letter)
    elif count > 1:
        print('There are', count, 'of the letter', letter)
    else:
        letterCountZeroList.append(letter)

print('There were none of the following letters found:')
for letter in letterCountZeroList:
    print(letter)
