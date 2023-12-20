import random


def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0

    while random_number != user_guess:
        user_guess = int(input(f"Guess a number between 1 and {x}:"))
        print(user_guess)
        if user_guess < random_number:
            print('your guess is too low')
        elif user_guess > random_number:
            print('your guess is too high')
        else:
            print('CORRECT!')


# guess(10)

def comp_guess(x):
    low = 1
    high = x
    feedback =''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"is {guess} too high (H), too low (L), or correct (C)?  ").lower()
        if feedback == 'h':
            high = guess -1
        if feedback == 'l':
            low = guess + 1
    print(f"YESS!!! the number was {guess}")     

comp_guess(555)
