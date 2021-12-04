#!/usr/bin/env python3

""" 
    version 1.12

    Program - generator haseł. Użytkownik podaje długość hasła a program wzraca wylosowane hasło.

    passwordGenerator(length) ==> hasło

    *** Chyba działa na testy nie było czasu, ale po co testować skoro domyślasz się że działa. ***
"""

import random
import os

values = [['1','2','3','4','5','6','7','8','9','0'],
          ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'],
          ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'],
          ['!','@','#','$','%','^','&','*','(',')','?']]

def passwordGenerator(length, i=0, password="", howMuchNumbers=0, howMuchLetters=0, howMuchBigLetters=0, howMuchSpecialSigns=0):
    if i == length:
        if howMuchNumbers == 0 or howMuchSpecialSigns == 0 or howMuchLetters == 0 or howMuchBigLetters == 0:
            password = ""
            return passwordGenerator(length, i=0)
        return password
    
    randomList = random.randint(0, 3)
    randomNumber = random.randint(0, len(values[randomList])-1)
    password += values[randomList][randomNumber]
    
    if values[randomList][randomNumber] in values[0]:
        howMuchNumbers += 1
    elif values[randomList][randomNumber] in values[1]:
        howMuchLetters += 1
    elif values[randomList][randomNumber] in values[2]:
        howMuchBigLetters += 1
    else:
        howMuchSpecialSigns += 1
    i += 1
    
    return passwordGenerator(length, i, password, howMuchNumbers, howMuchLetters, howMuchBigLetters, howMuchSpecialSigns)


while True:
    try:
        length = int(input("Podaj długość hasła (minimum 4 znaki, maximum 64 znaki): "))
        if length < 4 or length > 64:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            continue
    except ValueError:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        continue
    break

if __name__ == '__main__':
    print("\nOto twoje potężne hasło: " + passwordGenerator(length))