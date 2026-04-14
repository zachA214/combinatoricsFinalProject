'''
Project Notes

 - Password Generation
 - Calculates Entropy
 - Probabilities of being cracked within a timeframe
 - Probability of being cracked in a single guess
 - You may determine what the character space is (captials, lowercase, special characters, etc.)

 - Discuss history of entropy
'''
import sys
import random
import math
import time
from decimal import Decimal, getcontext

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import base64

lowercaseCharacters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

capitalCharacters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

specialCharacters = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', 
                     '_', '=', '+', '[', '{', '}', ']', '\\', '|', ';', ':', '\'', 
                     '\"', ',', '<', '.', '>', '/', '?']

numericalCharacters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

app = Flask(__name__)
CORS(app)

@app.route("/serverstatus", methods=["GET"])
def server_response():
    return jsonify({
        "reply": f"Server up as of {datetime.now().isoformat()}"
    })

@app.route("/www.entropyhistory", methods=["GET"])
def entropy_history():
    with open("imgs/rudolfcalusius.jpg", "rb") as f:
        encodedRudolf = base64.b64encode(f.read()).decode('utf-8') # make the image be able to be sent over flask
    with open("imgs/ludwigbotlzmann.jpg", "rb") as f:
        encodedLudwig = base64.b64encode(f.read()).decode('utf-8')
    with open("imgs/erwinschrödinger.jpg", "rb") as f:
        encodeedSchrödinger = base64.b64encode(f.read()).decode('utf-8')
    with open("imgs/claudeshannon.jpg", "rb") as f:
        encodedShannon = base64.b64encode(f.read()).decode('utf-8')
    return jsonify({
        "reply": f'''
        <div style="text-align: center;"> 

            <h1 style="font-size: 2.5rem;">History of Entropy</h1>

            <div style="width: 100%; overflow: hidden;">
                <div style="
                    float: left;
                    width: 100%;
                    padding: 10px;
                    height: 3000px;
                    background-color: #bbb;
                    box-sizing: border-box;
                ">
                    <h1>Rudolf Clausius</h1>
                    <p style="font-size: 18px;">In 1854, Rudolf Clausius, created the first concept of entropy. 
                    In comparison to modern mathematical and information based entropy, this entropy was in the realm of thermodynamics</p>
                    <br/>
                    <img src="data:image/png;base64,{encodedRudolf}" style = "height: 500px; width 350px;"> </> 
                    <p>Source: https://upload.wikimedia.org/wikipedia/commons/4/40/Clausius.jpg</p>
                    
                    <h1>Ludwig Boltzmann</h1>
                    <p style="font-size: 18px;">Later in 1877, Ludwig Boltzmann, developed a statisitcal mechanics appraoch to Clausius's definition.
                    In his idea, entropy is defined as "a statisical 'mixedupness' or disorder". This became the cornerstone of statisical mechanics.</p>
                    <img src="data:image/png;base64,{encodedLudwig}" style = "height: 500px; width 350px;"> </> 
                    <p>Source: https://en.wikipedia.org/wiki/Ludwig_Boltzmann#/media/File:Boltzmann2.jpg</p>

                    <h1>Erwin Schrödinger</h1>
                    <p style="font-size: 18px;">Much later in 1944, Erwin Schrödinger, adapted Boltzmanns interpretation of entropy 
                    in his book What is Life?. In simple terms, he defined that states of matter random distribution is lower when entropy is also lower</p>
                    <img src="data:image/png;base64,{encodeedSchrödinger}" style = "height: 500px; width 350px;"> </> 
                    <p>Source: https://en.wikipedia.org/wiki/Erwin_Schr%C3%B6dinger#/media/File:Erwin_Schr%C3%B6dinger_-_Narodowe_Archiwum_Cyfrowe_(1-E-939).jpg</p>

                    <h1>Claude Shannon</h1>
                    <p style="font-size: 18px;">Claude Shannon find something similar to classical entropy, Information Entropy. He came up with
                    the nconcept in 1948 while working at Bell Telephone. Information Entropy gives a value to the "average level of uncertainty
                    or information associated with the variable's potential states or possible outcomes". Then from Information Entropy we have
                    Password Entropy; which is the measure of how unpredicatable and difficult to guess a password is. To understand the output
                    of password entropy we get a value in bits, which can then be interpreted as being as strong as a string of that number of bits.
                    So a password with entropy 30, is as secure as a string of 30 randomly chosen bits (found by 2 to the power of 30) </p>
                    <img src="data:image/png;base64,{encodedShannon}" style = "height: 500px; width 350px;"> </> 
                    <p>Source: https://en.wikipedia.org/wiki/Claude_Shannon#/media/File:C.E._Shannon._Tekniska_museet_43069_(cropped).jpg</p>
                </div>
                Sources Used: <br>
                https://proton.me/blog/what-is-password-entropy <br>
                https://www.geeksforgeeks.org/computer-networks/password-entropy-in-cryptography/ <br>
                https://en.wikipedia.org/wiki/History_of_entropy <br>
                https://en.wikipedia.org/wiki/Password_strength#Entropy_as_a_measure_of_password_strength <br>
                https://www.okta.com/identity-101/password-entropy/
            </div>
        </div>
        '''
    })

@app.route("/www.passwordgenerator", methods=["GET"])
def generate_password():
    return jsonify({
        "reply": f'''
    <div style="text-align: center;">
    <h1> Password Generator </h1>
    </div>
    <div>
    <div style="max-width: 300px; display: flex; align-items: center; gap: 0.5rem">
        <label>Password Length:</label>
        <label>1</label>
        <input type="range" min="1" max="100" value="15" />
        <label>100</label>
    </div>
    </div>
    '''
    })

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-server".lower(): # if the user has 1 argument and it is exactly -server
        app.run(debug=True, host='0.0.0.0', port=5002)
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
    print("Generating password", end="", flush=True)
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.25)
    print()  # Move to the next line after progress indicator
    print(f"Generated Password of length {passLength}: {generatedPassword}")
    print(f"Number of possible combinations {int(math.pow(len(characterList), passLength))}")
    passEntropy = passwordEntropy(characterList, passLength)
    print(f"Password entropy: appx. {math.trunc(passEntropy)} bits")
    print(f"Password Strength: {defineEntropy(passEntropy)}")
    print(f"Time to Crack ({cracksPerSecond} per sec): appx. {calculateTimeToCrack(cracksPerSecond, characterList, passLength)}")
    print(f"Probability being cracked on first guess: {100 * calculateProbability(characterList, passLength, 1)}% chance")
    print(f"Probability being cracked within 1 month: {100 * calculateProbability(characterList, passLength, (cracksPerSecond * convertTimetoSeconds(1, "Month")))}% chance")
    return

def chooseCharacter(listOptions):
    character = random.randrange(0, len(listOptions))
    return listOptions[character]

''' 
Entropy Equation
E = L * log_2(R)

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

    upperBound = 99999999999999999999999999999999999999999999999999 #years
    lowerBound = 10 #seconds

    intervals = (
        ('years', 31557600),
        ('days', 86400),
        ('hours', 3600),
        ('minutes', 60),
        ('seconds', 1),
    )

    result = []
    for (name, count) in (intervals):
        value = total_seconds // count
        if (not result and name == "seconds" and value <= lowerBound): # return if time only has seconds and is less than lowerBound
            return "Practically instantly"
        if (value > 0):
            result.append(f"{int(value)} {name}") 
            total_seconds -= value * count
            if (name == "years" and value >= upperBound): # return if the amount of years is greater than upperBound
                return "More time than the universe has"

    if (not result):
        return "Instantly"
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
    N = Decimal(len(listOptions)) ** Decimal(generatedPassworedLength)
    guesses = Decimal(guessesMade)
    return guesses / N

# Each bit of entropy doubles the number of guesses needed to crack the password
# Or simply 2^E guessed needed to crack a password with E bits of entropy
# For example, 8 bits of entropy means 2^8 = 256 guesses needed to crack the password

def defineEntropy(passwordEntropyValue):
    if (not passwordEntropyValue): # Entropy not defined
        return "No password - No entropy"
    elif (passwordEntropyValue < 30): #Very weak
        return "Very weak"
    elif (passwordEntropyValue >= 30 and passwordEntropyValue < 50): #Weak
        return "Weak"
    elif (passwordEntropyValue >= 50 and passwordEntropyValue < 75): #Average
        return "Average"
    elif (passwordEntropyValue >= 75 and passwordEntropyValue < 120): #Strong
        return "Strong"
    elif (passwordEntropyValue >= 120): #Very strong
        return "Very strong"

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
    timeConversions = {
        "Minute" : 60,
        "Hour" : 3600,
        "Day" : 86400,
        "Week" : 604800,
        "Month" : 2629800,
        "Year" : 31557600
    }

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
        except:
           print("Invalid input please enter a number")


if __name__ == "__main__":
    main()