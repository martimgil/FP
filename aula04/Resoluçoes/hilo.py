# Complete the code to make the HiLo game.

import random

def playHiLo():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101)

    print("I picked a number between 1 and 100. Can you guess it?")
    while True:
        guess = int(input("Insira palpite: "))
        if guess == secret:
            print("Acertou!")
            break
        elif guess>secret:
            print("High")
        else:
            print("Low")

playHiLo()

