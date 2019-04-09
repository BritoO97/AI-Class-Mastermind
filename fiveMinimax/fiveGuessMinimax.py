import game
import time
import sys
from random import randint

originalSet = game.values[:]
def play():
     
    numGames = int(sys.argv[1])
    while(numGames > 0):
        
        unused = originalSet[:]
        workSet = originalSet[:]
        guess = "1122"
        
        startTime = time.time_ns()
        endTime = 0
        guesses = 0

        while True:

            unused.remove(guess)

            result = game.checkGuess(guess)
            guesses += 1
            #print(guess + " | " + result)

            if (result == "BBBB"):
                endTime = time.time_ns()
                print(guess + " " + str(guesses) + " " + str(endTime - startTime))
                break
    
            newSet = [] 

            for ans in workSet:
                if (validateGuess(guess, ans) == result):
                    newSet.append(ans)

            workSet = newSet

            #minimax step
            if (len(workSet) == 1):
                guess = workSet[0]
            else:
                default = 0
                scoreCount = {}
                score = {}
                maxS = None
                minS = None
                for possible in workSet:
                    for w in workSet:
                        
                        pegScore = validateGuess(possible, w)
                        if (scoreCount.get(pegScore, default) > 0):
                            scoreCount[pegScore] += 1
                        else:
                            scoreCount[pegScore] = 1
                    maxS = max(scoreCount)
                    score[possible] = scoreCount[maxS]
                    scoreCount = {}

                guess = min(score)
                
        
            if (len(workSet) < 1):
                endTime = time.time_ns()
                break

            #guess = workSet[randint(0, len(workSet) - 1)]

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
