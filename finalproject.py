'''
Project Notes

 - Password Generation
 - Calculates Entropy
 - Probabilities of being cracked within a timeframe
 - Probability of being cracked in a single guess
 - You may determine what the character space is (captials, lowercase, special characters, etc.)
 - User defined length / minimum and maximum lengths

 - Discuss history of entropy
'''
import sys
import random
import math

lowercaseCharacters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

capitalCharacters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

specialCharacters = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', 
                     '_', '=', '+', '[', '{', '}', ']', '\\', '|', ';', ':', '\'', 
                     '\"', ',', '<', '.', '>', '/', '?']

numericalCharacters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-server".lower(): # if the user has 1 argument and it is exactly -server
        print(f"{sys.argv[1]}")
        return
    cliProject() # Command line based
    return

def cliProject():
    generatedPassword = ""
    characterList = []
    passLength = max(0 , int(get_number("Select Length: ")))
    lowercase = get_bool("Has Lower? ")
    if (lowercase):
        characterList.extend(lowercaseCharacters)
    captial = get_bool("Has Captial? ")
    if (captial):
        characterList.extend(capitalCharacters)
    numerical = get_bool("Has Numbers? ")
    if (numerical):
        characterList.extend(numericalCharacters)
    special = get_bool("Has Special? ")
    if (special):
        characterList.extend(specialCharacters)
    
    if (not characterList):
        print("no chracter space chosen")
        return

    for _ in range(passLength):
        chosenItem = chooseCharacter(characterList)
        generatedPassword = generatedPassword + chosenItem
    print(f"Generated Password of length {passLength}: {generatedPassword}")
    print(f"Password entropy: appx. {math.trunc(passwordEntropy(characterList, passLength))} bits")
    print(f"Time to Crack ({passLength} per sec): appx. {math.trunc(calculateTimeToCrack(10000, characterList, passLength))} years")
    return

def chooseCharacter(listOptions):
    character = random.randrange(0, len(listOptions))
    return listOptions[character]

''' 
Entropy Equation
E = L × log_2(R)

E -> Password Entropy
L -> Number of characters (length of password)
R -> Number of options for each letter
'''
def passwordEntropy(listOptions, length):
    R = len(listOptions)
    return length * (math.log2(R))

'''
Crack Time Equation
          N
----------------------
X * 60 * 60 * 24 * 365

X -> Guesses per second
N -> Character space ^ length of password

'''
def calculateTimeToCrack(cracksPerSecond, listOptions, generatedPasswordLength):
    N = math.pow(len(listOptions), generatedPasswordLength)
    denom = cracksPerSecond * 60 * 60 * 24 * 365
    return N / denom

# Source - https://stackoverflow.com/a/32616663
# Posted by Joran Beasley, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-27, License - CC BY-SA 4.0

def get_bool(prompt):
    while True:
        try:
           return {"yes":True,"no":False}[input(prompt).lower()]
        except KeyError:
           print("Invalid input please enter Yes or No!")

def get_number(prompt):
    while True:
        try:
           return int(input(prompt))
        except KeyError:
           print("Invalid input please enter a number")


if __name__ == "__main__":
    main()