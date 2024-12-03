# Complete the code to make the HiLo game.

import random

def playHiLo():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101)

    print("I picked a number between 1 and 100. Can you guess it?")
    # put your code here
    guess = 0
    n = 0
    while (guess!=secret):
        guess = int(input("Guess: "))
        if guess>secret:
            print("High!")
        elif secret>guess:
            print("Low!")
        n+=1

    print("Done! {} attemps.".format(n))


playHiLo()
