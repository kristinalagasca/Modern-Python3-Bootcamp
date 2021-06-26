import random
import time


'''
Created this game as the first project. My goal was to have the computer play against itself for best 2 / 3.
If it reaches a tie, no points are given and it continues playing. The code will return which player wins at the end.
'''


p1_points = 0
p2_points = 0

while (p1_points or p2_points) <= 2:
    game = ['rock', 'paper', 'scissors']
    player1 = random.choice(game)
    player2 = random.choice(game)

    print('Ready? ...')
    time.sleep(1)
    print('ROCK ...')
    time.sleep(1)
    print('PAPER ...')
    time.sleep(1)
    print('SCISSORS ...')
    time.sleep(1)
    print('SHOOOOT!!')

    if player1 == player2:
        print('Player 1: ' + player1 + ', ' + 'Player 2: ' + player2)
        print('It\'s a tie! No points given.')
    elif player1 == 'rock':
        if player2 == 'paper':
            print('Paper covers rock! Player 2 wins!')
            p2_points += 1
        elif player2 == 'scissors':
            print('Rock smashes scissors! Player 1 wins!')
            p1_points += 1
    elif player1 == 'paper':
        if player2 == 'rock':
            print('Paper covers rock! Player 1 wins!')
            p1_points += 1
        elif player2 == 'scissors':
            print('Scissors cuts paper! Player 2 wins!')
            p2_points += 1
    elif player1 == 'scissors':
        if player2 == 'paper':
            print('Scissors cuts paper! Player 1 wins!')
            p1_points += 1
        elif player2 == 'rock':
            print('Rock smashes scissors! Player 2 wins!')
            p2_points += 1
    else:
        print('Error occurred. Exiting ...')
        break
    time.sleep(2)
