import game
from random import randint
import sys
import time

def randomGuess():
    numGames = int(sys.argv[1])
    while (numGames > 0):
        available = game.values[:]
        guesses = 0

        startTime = time.time_ns()
        endTime = 0
        while True:

            if (len(available) < 1):
                endTime = time.time_ns()
                break

            guessNum = randint(0, len(available)-1)
            guess = available[guessNum]
            available.remove(guess)

            guesses += 1
            result = game.checkGuess(guess)

            #print(guess + " | " + result)

            if (result == "BBBB"):
                endTime = time.time_ns()
                print(guess + " " + str(guesses) + " " + str(endTime - startTime))
                break
        numGames -= 1
        game.newAnswer()


randomGuess()


