# Candies game PVP

from random import randint

candies = 2021
n_player1 = False
n_player2 = False
n_total = 0
j = int(randint(1, 2)) # Draw
player1 = [0]
player2 = [0]
a = 0 # Candies to take
d = 0 # Rounds

def candies_game(player1, player2, n_player1, n_player2, a, d, candies, n_total, k, l):
    while candies > 0:
    # if j == 1: # Player1 moves first
        print(f'\nRound: {d + 1}')
        # print(f'candies on the table: {candies}\n')
        d += 1
        a = int(input(f'{k} takes candies : ')) # How many candies to take from the table
        n_player1 = True
        if (candies - a) > 0 and a <= 28: # Move of player1
            player1[0] = player1[0] + a
            n_player1 += 1
            n_total +=1
            candies = candies - a
            n_player1 = False
        elif a > 28:
            print(f'\nMaximum candies to take  - 28! Try again!')
            a = int(input('Enter number < 28: '))
            if (candies - a) > 0: # Move of player1
                player1[0] = player1[0] + a
                n_player1
                n_total += 1
                candies = candies - a
                n_player1 = False
        a = int(input(f'{l} takes candies : ')) # Move of player2
        n_player2 = True
        if (candies - a) > 0 and a <= 28: # Move of player2
            player2[0] = player2[0] + a
            n_player2
            n_total +=1
            candies = candies - a
            n_player2 = False
        elif a > 28:
            print(f'\nMaximum candies to take  - 28! Try again!')
            a = int(input('Enter number < 28: '))
            if (candies - a) > 0: # Move of player1
                player2[0] = player2[0] + a
                n_player2
                n_total += 1
                candies = candies - a
                n_player2 = False
        elif (candies - a) <= 0 and n_player1 == True: # Move of player1
            candies = candies
            # print(f'Bot took: {candies}')
            player1[0] = player1[0] + candies + player2[0]
            n_player1 = False
            n_total += 1
            print(f'\nGAME OVER! {k} takes last {candies} candies from the table and {player2[0]} of {l} candies')
            # print(f'{k} candies: {player1}')
            # print(f'{l} candies: {player2}')
            print(f'Total moves: {n_total}\n')
            break
        elif (candies - a) <= 0 and n_player2 == True: # Move of player2
            candies = candies
            # print(f'Bot took: {candies}')
            player2[0] = player2[0] + candies + player1[0]
            n_player2 = False
            n_total += 1
            print(f'\nGAME OVER! {l} takes last {candies} candies from the table and {player1[0]} of {k} candies')
            # print(f'{k} candies: {player1}')
            # print(f'{l} candies: {player2}')
            print(f'Total moves: {n_total}\n')
            break

if j == 1:
    print('\nPlayer1 moves firtst')
    k = 'Player1'
    l = 'Player2'
    candies_game(player1, player2, n_player1, n_player2, a, d, candies, n_total, k, l)
elif j == 2:
    print('\nPlayer2 moves first')
    k = 'Player2'
    l = 'Player1'
    candies_game(player1, player2, n_player1, n_player2, a, d, candies, n_total, k, l)