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
    cracksPerSecond = 10000
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
    print(f"Number of possible combinations {math.pow(len(characterList), passLength)}")
    print(f"Password entropy: appx. {math.trunc(passwordEntropy(characterList, passLength))} bits")
    print(f"Time to Crack ({cracksPerSecond} per sec): appx. {calculateTimeToCrack(cracksPerSecond, characterList, passLength)}")
    print(f"Probability being cracked on first guess: {100 * calculateProbability(characterList, passLength, 1)}% chance")
    print(f"Probability being cracked within x [time period]")
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
    
    total_passwords = math.pow(len(listOptions), generatedPasswordLength)

    total_seconds = total_passwords / cracksPerSecond

    intervals = (
        ('years', 31557600),
        ('days', 86400),
        ('hours', 3600),
        ('minutes', 60),
        ('seconds', 1),
    )

    result = []
    for name, count in intervals:
        value = total_seconds // count
        if value > 0:
            result.append(f"{int(value)} {name}")
            total_seconds -= value * count

    if not result:
        return "0 seconds"
    return ', '.join(result)

'''
The equation for correct guesses
  m
-----
 N^L

m -> total guesses
N -> Character space
L -> Length of password
'''
# We can find guesses in a time frame by multiplying
# The number of guesses per second by the time alloted in seconds

def calculateProbability(listOptions, generatedPassworedLength, guessesMade):
    return guessesMade / math.pow(len(listOptions), generatedPassworedLength)

'''
Time in Seconds for each
Minute : 60
Hour : 3600
Day : 86400
Week : 604800
Month : 2629800
Year : 31557600
'''

def convertTimetoSeconds(time, format):
    timeConversions = [
        {"Minute" : 60},
        {"Hour" : 3600},
        {"Day" : 86400},
        {"Week" : 604800},
        {"Month" : 2629800},
        {"Year" : 31557600}
    ]

    if (format not in timeConversions):
        return -1

    return time * timeConversions[format]

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