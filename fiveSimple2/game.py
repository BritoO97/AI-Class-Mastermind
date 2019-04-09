#!/usr/bin/python3

from random import randint

values = []

for num1 in range(1, 7):
    for num2 in range(1, 7):
        for num3 in range(1, 7):
            for num4 in range(1, 7):
                newVal = str(num1) + str(num2) + str(num3) + str(num4)
                values.append(newVal)
answer = -1

def newAnswer():
    global answer
    answer = values[randint(0, 1295)]

newAnswer()

def checkGuess (guessStr):
    result = ""
    tempAns = list(answer[:])
    guess = list(guessStr)
    if (len(guess) > 4):
        return result

    for i in range(0,len(guess)):
        if (guess[i] == tempAns[i]):
            result += "B"
            tempAns[i] = "X"
        elif (guess[i] != tempAns[i] and guess[i] in tempAns):
            temp = tempAns.index(guess[i])
            if (guess[temp] == tempAns[temp]):
                    result += "B"
                    tempAns[temp] = "X"
                    guess[temp] = "Y"
            else:
                result += "W"

    return result




