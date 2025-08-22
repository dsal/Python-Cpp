import random
answer = random.randint(1,99)
guess = input('Say my number?')
guess = int(guess)
while guess != answer:
    if guess > answer:
        print ("Mine is smaller")
    else:
        print ("Mine is bigger")
    guess = input('Say my number?')
    guess = int(guess)
print ("YOU'RE GODDAMN RIGHT!")




"""
This code implements a number-guessing game.
A random integer between 1 and 99 is generated,
and the user is prompted to guess the number.
Iterative feedback is provided until the user correctly identifies the generated number.
"""