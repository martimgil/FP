# Complete the code to make the HiLo game.

import random

def playHiLo():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101)
    tentativas = 0
    print("I picked a number between 1 and 100. Can you guess it?")
    # put your code here
    while True:
        guess = int(input("Guess: "))
        tentativas+=1


        if guess==secret:
            print("Acertou!", tentativas, "tentativas.")
            break
        else:
            if guess>secret:
                print("Alto")
            elif guess<secret:
                print("Baixo")




playHiLo()

