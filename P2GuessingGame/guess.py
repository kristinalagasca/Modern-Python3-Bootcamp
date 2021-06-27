from random import randint

x = randint(1, 10)
guess = None

while True:
    guess = input('pick a number between 1 and 10: ')
    guess = int(guess)
    if guess < x:
        print('too low!')
    elif guess > x:
        print('too high')
    else:
        print('good job!')
        play_again = input('would you like to play again? (y/n): ')
        if play_again == 'y':
            x = randint(1, 10)
            guess = None
        else:
            print('thanks for playing!')
            break
