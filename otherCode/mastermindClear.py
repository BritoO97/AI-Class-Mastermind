# source: https://github.com/catlzy/knuth-mastermind/blob/master/Mastermind.py
# retrieved for the minimax Step

from __future__ import print_function
from __future__ import division  # this ensures the / operation give floats by default
import itertools

'''
This function compares a guess and a code and returns (numCorrect,numTransposed)
which correspond to the number of black and white pegs returned in Mastermind.
The code is a global variable, which the KnuthFive() function cannot use.
'''
def evaluate_guess(guess):
    global code

	# Get the length n of the guess and the code.
    assert(len(guess) == len(code))
    n = len(guess)

    # Determine the correct and incorrect positions.
    correct_positions = [i for i in list(range(n)) if guess[i] == code[i]]
    incorrect_positions = [i for i in list(range(n)) if guess[i] != code[i]]
    num_correct = len(correct_positions)

    # Reduce the guess and the code by removing the correct positions.
    # Create the set values that are common between the two reduced lists.
    reduced_guess = [guess[i] for i in incorrect_positions]
    reduced_code = [code[i] for i in incorrect_positions]
    reduced_set = set(reduced_guess) & set(reduced_guess)

    # Determine the number of transposed values.
    num_transposed = 0
    for x in reduced_set:
    	num_transposed += min(reduced_guess.count(x), reduced_code.count(x))

    return num_correct, num_transposed


'''
This function compares a guess and a temporary code and returns (numCorrect,numTransposed)
which correspond to the number of black and white pegs returned in Mastermind.
This function is created becuse actual code cannot be accessed in KnuthFive()
'''
def evaluation_inner(guess, fakeCode):

	# Get the length n of the guess and the code.
    assert(len(guess) == len(fakeCode))
    n = len(guess)

    # Determine the correct and incorrect positions.
    correct_positions = [i for i in list(range(n)) if guess[i] == fakeCode[i]]
    incorrect_positions = [i for i in list(range(n)) if guess[i] != fakeCode[i]]
    num_correct = len(correct_positions)

    # Reduce the guess and the fakeCode by removing the correct positions.
    # Create the set values that are common between the two reduced lists.
    reduced_guess = [guess[i] for i in incorrect_positions]
    reduced_code = [fakeCode[i] for i in incorrect_positions]
    reduced_set = set(reduced_guess) & set(reduced_guess)

    # Determine the number of transposed values.
    num_transposed = 0
    for x in reduced_set:
    	num_transposed += min(reduced_guess.count(x), reduced_code.count(x))

    return num_correct, num_transposed


'''
Implement Knuth's algorithm here.
You cannot use the global variable code.
'''
def KnuthFive():
    # all the 1296 possible codes
    allP = [tuple(x) for x in itertools.product(range(1,7), repeat=4)]

    # the list contains all remaining possible solutions
    S = [tuple(x) for x in itertools.product(range(1,7), repeat=4)]

    # the following lines create a list (allScore) of all possible peg scores
    # allstemp is created because (3,1) is not allowed and thus is used for slicing later
    allstemp = []
    for i in range(5):
        for j in range(0, 4-i+1):
            allstemp.append((i, j))
    allScore = allstemp[:len(allstemp)-2]+allstemp[len(allstemp)-1:]

    # initial guess
    guess = (1,1,2,2)
    guessList = [guess]
    num_correct, num_transposed = evaluate_guess(guess)

    # while the guess is not the code, keep guessing
    while (num_correct, num_transposed) != (4, 0):
        # temp is the list after removing all the conflicting guesses in S
        temp = []
        # cScore is a list of scores for each guess in allP
        cScore = []*len(allP)

        # remove gueses from S that will not give the same peg score if it is the answer
        for item in S:
            if evaluation_inner(guess, item) == (num_correct, num_transposed):
                temp.append(item)
        S = temp[:]

        # minimax step of the algorithm
        # for all unused guesses in allP, create a list (hitCount) that will be used
        # to calculate the score for the guess
        for item in allP:
            if item not in guessList:
                hitCount = [0]*len(allScore)
                # for all guesses in S, calculate its peg score if the unused guess in allP
                # is the answer. Increase the corresponding position in hitCount by 1
                for s in S:
                    hitCount[allScore.index(evaluation_inner(s, item))] += 1
                # calculate the score for the current unused guess
                cScore.append(len(S)-max(hitCount))
            else:
                cScore.append(0)
        # find all indices with the max score
        maxScore = max(cScore)
        indices = [i for i, x in enumerate(cScore) if x == maxScore]
        # if any guesses corresponds to the indices is a member of S, use that as the next guess
        change = False
        for i in range(len(indices)):
            if allP[indices[i]] in S:
                guess = allP[indices[i]]
                change = True
                break
        # else use the smallest guess as next guess
        if change == False:
            guess = allP[indices[0]]
        guessList.append(guess)
        num_correct, num_transposed = evaluate_guess(guess)

    return guessList


if __name__ == "__main__":
    global code

    # Create all 1296 possible Mastermind codes.
    allCodes = [tuple(x) for x in itertools.product(range(1,7), repeat=4)]

    # Initialize statistics.
    totalSolved = 0    # number of the 1296 codes that you solved
    totalUnsolved = 0  # number of the 1296 codes that you didn't solve
    worstCase = 0      # largest number of guesses used to solve a code
    totalGuesses = 0   # total number of guesses used to solve all solved codes

    for code in allCodes:
        guessList = KnuthFive()
        if guessList[-1] == code:
            totalSolved += 1
            numGuesses = len(guessList)
            worstCase = numGuesses if numGuesses > worstCase else worstCase
            totalGuesses += numGuesses
        else:
            totalUnsolved += 1

    print("total solved: %d" % totalSolved)
    print("worst case: %d" % worstCase)
    print("average: %f" % (totalGuesses/totalSolved))
    print("total unsolved: %d" % totalUnsolved)
