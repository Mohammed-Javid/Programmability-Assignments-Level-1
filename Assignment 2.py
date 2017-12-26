import sys
import random

Guess = random.randint(1,10)

a = input ( ' Guess a number between 1 to 10 : ' )

A=int(a)

if A==Guess:
    print('Whooo!!! you won')
else:
    if A<Guess:
        print('You are lazy')
    else:
        if A>Guess:
            print('You are running')

        
        
