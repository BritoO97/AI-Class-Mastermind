import game
import time
import sys
from random import randint

originalSet = game.values[:]
def play():
     
    numGames = int(sys.argv[1])
    while(numGames > 0):
        
        guessList = []

        allP = originalSet[:]
        workSet = originalSet[:]
        guess = "1122"
        
        startTime = time.time_ns()
        endTime = 0
        guesses = 0

        allstemp = []
        for i in range(5):
            for j in range(0, 4-i+1):
                allstemp.append((i, j))
        allScore = allstemp[:len(allstemp)-2]+allstemp[len(allstemp)-1:]

        while True:
            
            guessList.append(guess)

            temp = []
            cScore = []*len(allP)

            result = game.checkGuess(guess)
            guesses += 1
            #print(guess + " | " + result)

            if (result == "BBBB"):
                endTime = time.time_ns()
                print(guess + " " + str(guesses) + " " + str(endTime - startTime))
                break
    
            newSet = []

            for ans in workSet:
                if ans not in guessList:
                    if (validateGuess(guess, ans) == result):
                        newSet.append(ans)

            workSet = newSet

            for item in allP:
                if item not in guessList:
                    hitCount = [0]*len(allScore)
                    for s in workSet:
                        evalResult = validateGuess(s, item)
                        countProper = evalResult.count("B")
                        countTransposed = evalResult.count("W")
                        #print(str(countProper) + " | " + str(countTransposed))
                        #print (str(allScore.index(countProper, countTransposed)))

                        #if (hitCount.get(countProper, 0) > 0):
                            #scoreCount[pegScore] += 1
                        #else:
                            #scoreCount[pegScore] = 1

                        hitCount[allScore.index((countProper, countTransposed))] += 1
                    cScore.append(len(workSet)-max(hitCount))
                else:
                    cScore.append(0)

            maxScore = max(cScore)
            indices = [i for i, x in enumerate(cScore) if x == maxScore]

            change = False
            for i in range(len(indices)):
                if allP[indices[i]] in workSet:
                    guess = allP[indices[i]]
                    change = True
                    break
            if change == False:
                guess = allP[indices[0]]                            
        
            if (len(workSet) < 1):
                endTime = time.time_ns()
                break

        numGames -= 1
        game.newAnswer()
       




def validateGuess(guessStr, supposed):
    result = ""
    tempAns = list(supposed[:])
    guess = list(guessStr)
    if (len(guess) > 4):
        return result

    for i in range(0, len(guess)):
        if(guess[i] == tempAns[i]):
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

play()
