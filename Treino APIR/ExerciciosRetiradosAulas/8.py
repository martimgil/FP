# Complete the code to make the HiLo game.

import random

def playHiLo():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    attemp = 0
    print("I picked a number between 1 and 100. Can you guess it?")
    # put your code here
    while True:
        guess = int(input("Guess?"))
        attemp += 1
        if guess == secret:
            break
        elif guess>secret:
            print("High")
        else:
            print("Low")
    print("Win! {} tries.".format(attemp))


playHiLo()

