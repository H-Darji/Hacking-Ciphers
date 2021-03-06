# Affine Cipher
# Source: http://inventwithpython.com/hacking (BSD Licensed)
# Modified by: Harshil Darji (github.com/H-Darji)

import sys, pyperclip, random, cryptomath_module as cryptoMath

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def main():
    message = input('Enter message: ')
    key = int(input('Enter key [2000 - 9000]: '))
    mode = input('Encrypt/Decrypt [E/D]: ')

    if mode.lower().startswith('e'):
              mode = 'encrypt'
              translated = encryptMessage(key, message)
    elif mode.lower().startswith('d'):
              mode = 'decrypt'
              translated = decryptMessage(key, message)
    print('\n%sed text: \n%s' % (mode.title(), translated))
    pyperclip.copy(translated)
    print('Full text copied to clipboard')

def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('The affine cipher becomes weak when key A is set to 1. Choose different key')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('The affine cipher becomes weak when key A is set to 1. Choose different key')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
    if cryptoMath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A %s and the symbol set size %s are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))

def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    cipherText = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            cipherText += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            cipherText += symbol
    return cipherText

def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plainText = ''
    modInverseOfkeyA = cryptoMath.findModInverse(keyA, len(SYMBOLS))
    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            plainText += SYMBOLS[(symIndex - keyB) * modInverseOfkeyA % len(SYMBOLS)]
        else:
            plainText += symbol
    return plainText

def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
    if cryptoMath.gcd(keyA, len(SYMBOLS)) == 1:
        return keyA * len(SYMBOLS) + keyB

if __name__ == '__main__':
    main()
