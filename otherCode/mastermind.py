# Source https://gist.github.com/igor-panteleev
# Used for the Minimax Code.

import argparse
import itertools
import random


def score(self, other, options):
    first = len([a for a, b in zip(self, other) if a == b])
    second = sum(min(self.count(i), other.count(i)) for i in options) - first
    return first, second


def _test_guess(guess, secret, options):
    return score(secret, guess, options)


def _real_guess():
    while True:
        inp = input('Your result in format XY: ')
        try:
            res = tuple(map(int, inp))
        except ValueError:
            print('Input is not a digits.')
            continue

        if len(res) != 2:
            print('Result should has 2 digits.')
            continue

        return res


def make_guess(guess, options, secret=None):
    print('Guess {}'.format(str(guess)))
    if secret is not None:
        return _test_guess(guess, secret, options)
    else:
        return _real_guess()


def main(n_options=6, n_statements=4, secret=None):
    if secret is not None:
        if len(secret) != n_statements:
            raise ValueError(
                'Number of test values should be equal to number of statements.'
            )
        secret = tuple(map(int, secret))
        if max(secret) > n_options - 1:
            raise ValueError(
                'Test values should be from 0 to {}'.format(n_options - 1))
        print('Running in test mode.')

    # prepare data
    options = tuple(range(n_options))

    possible = frozenset(itertools.product(options, repeat=n_statements))

    S = set(possible)

    results = []
    for right in range(n_statements + 1):
        for wrong in range(n_statements + 1 - right):
            if not (right == n_statements - 1 and wrong == 1):
                results.append((right, wrong))

    # first guess
    guess = []
    for i in range(n_statements // 2):
        while True:
            char = random.choice(options)
            if char not in guess:
                break
        guess.extend(itertools.repeat(char, 2))

    if n_statements % 2:
        guess.append(random.choice(options))

    # guess loop
    while True:
        res = make_guess(guess, options, secret)

        if res[0] == n_statements:
            print('You won!')
            break

        remove = set(g for g in S if score(g, guess, options) != res)
        S.difference_update(remove)

        # get next guess
        if len(S) == 1:
            guess = S.pop()
        else:
            # minimax
            max_s_v = 0
            max_s_g = None
            for p in possible:
                min_s = float('inf')
                for r in results:
                    s = sum(score(g, p, options) != r for g in S)
                    min_s = min(min_s, s)

                if min_s > max_s_v:
                    max_s_v = min_s
                    max_s_g = p

            guess = max_s_g


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', type=int, default=6, metavar='O',
                        dest='n_options', help='Number of possible options.')
    parser.add_argument('-s', type=int, default=4, metavar='S',
                        dest='n_statements', help='Number of statements.')
    parser.add_argument('-t', type=str, metavar='XXXX', dest='secret',
                        help='Test algorithm with this value as secret.')

    args = parser.parse_args()
    main(**vars(args))
