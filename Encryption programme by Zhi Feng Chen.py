# Caesar Cipher Programme By Zhi Feng Chen
# Create Lists

global counter
global numberOfCharacters
counter = 0
finalList = []
encryptedLetters = []
shiftedCharacters = []
dataList = []
invalidCharacterPosition = []
invalidCharacters = []
history = open("history.txt", 'a+')  # Opens the history find in appending mode

# Extended letters lists
# (can be modified and ONLY ONE list can be active at a time)
# But cannot have duplicate character or letters reguardless
# of case as it breaks the programme

letters = ['s', '/', 'y', '{', 'v', '?', 'a', 'b', 'c', 'd', 'e',
          '#', 'g', 'h', 'i', '&', 'k', 'l', 'm', '%', 'o',
          '@', ' ', '!', '.', ':', ';', '*', '_', '-', "'", '+',
          '"', '=', 'f', 'n', '$', '^', 'j', ')', '(']

#letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           #'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           #'u', 'v', 'w', 'x', 'y', 'z']

numberOfCharacters = (len(letters) - 1)


def showHistory(history):
    print('\n')
    print('Encryption History')
    for line in history:
        cipher, s = line.split(' Key used: ')
        print('Encrypted Text: ', cipher)
        print('Key Shift: ', s)

# reading and writing to files


def outputEncryptedData(data, s):
    history.write(str(data + ' Key used: '))
    history.write(str(str(s) + '\n'))
    history.seek(0)


# checking if the user wants to start or end programme


def continueOrEndCheck():
    while True:
        try:
            continueOrEnd = input("Please press ENTER to start "
                                  "programme or type E to exit "
                                  "programme and show history: ")
            if continueOrEnd == '':
                return ('continue')
            if continueOrEnd.lower() == 'e':
                return 'exit'
            print("INVALID INPUT")
            continue
        except:
            print('INVALID INPUT')

# definition to check if the input key is an integer


def encryptCheckKey():
    while True:
        try:
            key = input('Please enter a key to encrypt your message: ')
            key = int(key)
            return key
        except:
            print('please enter a INTEGER key!')


def decryptCheckKey():
    while True:
        try:
            key = input('Please your decryption key: ')
            key = int(key)
            return key
        except:
            print('please enter a INTEGER key!')

# asks for the user to select encryption or decryption


def checkEncryption():
    while True:
        try:
            encryptionOrDecryption = input('Type E for encryption '
                                           'or D for decryption: ')
            encryptionOrDecryption = encryptionOrDecryption.lower()
            if encryptionOrDecryption == 'encrypt' or \
               encryptionOrDecryption == 'decrypt':
                return encryptionOrDecryption
            if encryptionOrDecryption == 'e' or encryptionOrDecryption == 'd':
                return encryptionOrDecryption
            else:
                print('Invalid Input')
                continue
        except:
            print('Invalid Input')

    # Asks for input data, converts all letters into
    # lowercase letters stores it in variable and list
    # Asks for an input key and checks that it is an
    # integers and store it in a variable


def ifEncryption():
    while True:
        try:
            inputData = input("please enter the data to be encrypted: ")
            if inputData == "" or inputData == " ":
                print('Invalid Output')
                continue
            inputKey = encryptCheckKey()
            print("Your chosen encryption key is", inputKey)
            print("Your decryption key is", inputKey)
            return inputData, inputKey
        except:
            print('Invalid Input')


def ifDecryption():
    while True:
        try:
            inputData = input("please enter the data to be decrypted: ")
            if inputData == "" or inputData == " ":
                print('Invalid Output')
                continue
            inputKey = decryptCheckKey()
            print("Your chosen decryption key is", inputKey)
            inputKey = inputKey * -1
            return inputData, inputKey
        except:
            print('Invalid Input')


def encryptionProgramme(encryptionOrDecryption):
    # clears all temporary lists and variables
    counter = 0
    finalList = []
    encryptedLetters = []
    shiftedCharacters = []
    dataList = []
    invalidCharacterPosition = []
    invalidCharacters = []
    # Asks for input data, converts all letters
    # into lowercase letters stores it in variable and list
    if encryptionOrDecryption == 'encrypt' or encryptionOrDecryption == 'e':
        inputData, inputKey = ifEncryption()
    if encryptionOrDecryption == 'decrypt' or encryptionOrDecryption == 'd':
        inputData, inputKey = ifDecryption()
    dataList = list(inputData.lower())
    # print(inputKey)

    # find index of character in the letters list
    for character in dataList:
        if character not in letters:
            invalidCharacters.append(character)
            invalidCharacterPosition.append(counter)
            counter += 1
            continue
        index = letters.index(character)
        # print(index)
        shiftedCharacters.append(index)
        counter += 1
    # print(dataList)
    # print(shiftedCharacters)
    # encryption of the data to cipher text
    for index in shiftedCharacters:
        newIndex = index + inputKey
        while newIndex > numberOfCharacters:
            difference = (newIndex - numberOfCharacters)
            newIndex = 0
            newIndex = newIndex + (difference - 1)
            # print(difference, newIndex)
    # decryption
        while newIndex < (numberOfCharacters * -1):
            difference = (newIndex + (numberOfCharacters + 1))
            newIndex = 0
            newIndex = newIndex + (difference)
    # print(difference, newIndex)
        encryptedLetters.append(newIndex)

    # appends each encrypted index to a list
    # takes the third encryptedLetters index and takes
    # that index of letters list and appends it to the finalList
    for letter in range(0, len(encryptedLetters)):
        finalList.append(letters[encryptedLetters[letter]])
    # print(encryptedLetters)
    if len(invalidCharacters) > 0:
        for INDEX in range(0, len(invalidCharacters)):
            finalList.insert(invalidCharacterPosition[INDEX],
                             invalidCharacters[INDEX])
    print("Output: ", *finalList, sep='')
    encryptedText = ''.join(finalList)
    return encryptedText, inputKey


# prints starting banner
print("""CAESAR CIPHER PROGRAMME
By Zhi Feng Chen
NOTE: THE DECRYPTION KEY WILL BE THE
SAME AS THE KEY USED FOR ENCRYPTION
""")

# loops through the programme

while True:
    # asks to start or end programme
    continueOrEnd = continueOrEndCheck()
    # if start programme then it runs checkEncryption()
    # otherwise the programme closes
    if continueOrEnd == 'continue':
        encryptionOrDecryption = checkEncryption()
        encryptedText, inputKey = encryptionProgramme(encryptionOrDecryption)
        outputEncryptedData(encryptedText, inputKey)  # encrypted text # key
    elif continueOrEnd == 'exit':
        break
    print()

showHistory(history)
print('Closing programme....')
input()
