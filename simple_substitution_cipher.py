# Simple Substitution Cipher
# Source: http://inventwithpython.com/hacking (BSD Licensed)
# Modified by: Harshil Darji (github.com/H-Darji)

import pyperclip, sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message = input('Enter message: ')
    key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    resp = input('Encrypt/Decrypt [e/d]: ')

    checkValidKey(key)

    if resp.lower().startswith('e'):
        mode = 'encrypt'
        translated = encryptMessage(key, message)
    elif resp.lower().startswith('d'):
        mode = 'decrypt'
        translated = decryptMessage(key, message)

    print('\nCopying %sion to clipboard:' % mode.title())
    print('%s' % translated)
    pyperclip.copy(translated)

def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    if keyList != lettersList:
        sys.exit('Error in the key or symbol set.')

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key

    if mode == 'decrypt':
        charsA, charsB = charsB, charsA
        
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol

    return translated

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()
