encodeDict = {'a': '=', 'b': '(', 'c': ')', 'd': ',', 'e': '/', 'f': '|', 'g': '7', 'h': '8', 'i': '9', 'j': '*',
                  'k': '<', 'l': '4', 'm': '5', 'n': '6', 'o': '-', 'p': ';', 'q': '1', 'r': '2', 's': '3', 't': 't',
                  'u': '+', 'v': '0', 'w': '.', 'x': 'x', 'y': 'y', 'z': 'z', '.': '>', ',': '[', ' ': ']'}

decodeDict = {'=': 'a', '(': 'b', ')': 'c', ',': 'd', '/': 'e', '|': 'f', '7': 'g', '8': 'h', '9': 'i', '*': 'j',
                  '<': 'k', '4': 'l', '5': 'm', '6': 'n', '-': 'o', ';': 'p', '1': 'q', '2': 'r', '3': 's', 't': 't',
                  '+': 'u', '0': 'v', '.': 'w', 'x': 'x', 'y': 'y', 'z': 'z', '>': '.', '[': ',', ']': ' '}


def encodeChar(char):

    return encodeDict[char]


def decodeChar(char):

    return decodeDict[char]


def encodeString(string):

    encodedString = ''

    for i in range(0, len(string)):

        encodedString += encodeChar(string[i])

    return encodedString


def decodeString(string):

    decodedString = ''

    for i in range(0, len(string)):

        decodedString += decodeChar(string[i])

    return decodedString


StringToEncode = 'hello'

print(StringToEncode)

ECString = encodeString(StringToEncode)

print(ECString)

StringToDecode =ECString
DCString = decodeString(StringToDecode)

print(DCString)