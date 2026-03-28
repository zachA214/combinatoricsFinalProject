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

lowercaseCharacters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

capitalCharacters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

specialCharacters = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', 
                     '_', '=', '+', '[', '{', '}', ']', '\\', '|', ';', ':', '\'', 
                     '\"', ',', '<', '.', '>', '/', '?']
def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-server".lower(): # if the user has 1 argument and it is exactly -server
        print(f"{sys.argv[1]}")
        return
    cliProject() # Command line based
    return

def cliProject():
    generatedPassword = ""
    characterList = []
    length = max(0 , int(input("Select Length: ")))
    lowercase = get_bool("Has Lower? ")
    if (lowercase):
        characterList.extend(lowercaseCharacters)
    captial = get_bool("Has Captial? ")
    if (captial):
        characterList.extend(capitalCharacters)
    special = get_bool("Has Special? ")
    if (special):
        characterList.extend(specialCharacters)
    

    for _ in range(length):
        chosenItem = chooseCharacter(characterList)
        generatedPassword = generatedPassword + chosenItem
    print(f"{generatedPassword}")
    return

def chooseCharacter(listOptions):
    character = random.randint(0, len(listOptions))
    return listOptions[character]

# Source - https://stackoverflow.com/a/32616663
# Posted by Joran Beasley, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-27, License - CC BY-SA 4.0

def get_bool(prompt):
    while True:
        try:
           return {"true":True,"false":False}[input(prompt).lower()]
        except KeyError:
           print("Invalid input please enter True or False!")

def get_number(prompt):
    while True:
        try:
           return int(input(prompt))
        except KeyError:
           print("Invalid input please enter a positive number")


if __name__ == "__main__":
    main()