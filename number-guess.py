import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f'Guess a number between 1 and {x}'))
        print(f"{guess}")
        if guess < random_number:
            print('Sorry,guess again.Too low')
        elif guess > random_number:
            print('sorry,guess again.Too high')

    print('Good work,you have guessed the number!')
guess(10)