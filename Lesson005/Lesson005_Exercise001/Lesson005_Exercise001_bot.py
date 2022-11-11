# Candies game PVE

from random import randint

candies = 200
n_player = 0
n_bot = 0
n_total = n_player + n_bot
j = int(randint(1, 2))
player = [0]
bot = [0]
a = 0
d = 0

if j == 1:
    print('\nPlayer moves firtst')
elif j == 2:
    print('\nBot moves first')

while candies > 0:
    if j == 1: # Player moves first
        print(f'\nRound: {d + 1}')
        print(f'candies on the table: {candies}\n')
        d += 1
        a = int(input('Enter number < 28: ')) # How many candies to take from the table
        # a = int(randint(0, 28))
        if (candies - a) > 0: # Move of player
            # a = int(randint(0, 28))
            # print(f'a: {a}')
            player[0] = player[0] + a
            n_player += 1
            n_total = n_player + n_bot
            candies = candies - a
            # print(f'player first: n_player-{n_player}, candies-{candies}, player-{player}')
            # print(f'candies on the table: {candies}')
            a = int(randint(0, 28))
            if (candies - a) > 0: # Move of bot
                print(f'Bot took: {a}')
                bot[0] = bot[0] + a
                n_bot += 1
                n_total = n_player + n_bot
                candies = candies - a
                # print(f'player first: n_bot-{n_bot}, candies-{candies}, bot-{bot}')
                # print(f'candies on the table: {candies}')
            elif (candies - a) <= 0: # Move of bot
                candies = candies
                print(f'Bot took: {candies}')
                bot[0] = bot[0] + candies
                n_bot += 1
                n_total = n_player + n_bot
                # print(f' else player first: n_bot-{n_bot}, candies-{candies}, bot-{bot}')
                # print(f'candies on the table: {candies}')
                print(f'\nGAME OVER! Bot takes last {candies} candies')
                print(f'Player candies: {player}')
                print(f'Bot candies: {bot}')
                print(f'Total moves: {n_total}\n')
                break
        elif (candies - a) <= 0: # Move of player
            candies = candies
            # print(f'Bot took: {candies}')
            player[0] = player[0] + candies
            n_player += 1
            n_total = n_player + n_bot
            # print(f' else player first: n_player-{n_player}, candies-{candies}, player-{player}')
            # print(f'candies on the table: {candies}')
            print(f'\nGAME OVER! Player takes last {candies} candies')
            print(f'Player candies: {player}')
            print(f'Bot candies: {bot}')
            print(f'Total moves: {n_total}\n')
            break
    elif j == 2: # Bot moves first
        print(f'\nRound: {d + 1}')
        print(f'candies on the table: {candies}\n')
        d += 1
        a = int(randint(0, 28))
        if (candies - a) > 0: # Move of bot
            # a = int(randint(0, 28))
            print(f'Bot took: {a}')
            bot[0] = bot[0] + a
            n_bot += 1
            n_total = n_player + n_bot
            candies = candies - a
            # print(f'bot first: n_bot-{n_bot}, candies-{candies}, bot-{bot}')
            # print(f'candies on the table: {candies}')
            # a = int(randint(0, 28))
            a = int(input('Enter number < 28: '))
            if (candies - a) > 0: # Move of player
                # print(f'a: {a}')
                player[0] = player[0] + a
                n_player += 1
                n_total = n_player + n_bot
                candies = candies - a
                # print(f'bot first: n_player-{n_player}, candies-{candies}, player-{player}')
                # print(f'candies on the table: {candies}')
            elif (candies - a) <= 0: # Move of player
                candies = candies
                # print(f'a: {a}')
                player[0] = player[0] + candies
                n_player += 1
                n_total = n_player + n_bot
                # print(f' else bot first: n_bot-{n_player}, candies-{candies}, bot-{player}')
                # print(f'candies on the table: {candies}')
                print(f'\nGAME OVER! Player takes last {candies} candies')
                print(f'Player candies: {player}')
                print(f'Bot candies: {bot}')
                print(f'Total moves: {n_total}\n')
                break                
        elif (candies - a) <= 0:
            candies = candies
            # print(f'Bot took: {candies}')
            bot[0] = bot[0] + candies
            n_bot += 1
            n_total = n_player + n_bot
            # print(f' else bot first: n_bot-{n_bot}, candies-{candies}, bot-{bot}')
            # print(f'candies on the table: {candies}')
            print(f'\nGAME OVER! Bot takes last {candies} candies')
            print(f'Player candies: {player}')
            print(f'Bot candies: {bot}')
            print(f'Total moves: {n_total}\n')
            break

if player[0] > bot[0]:
    print(f'Player wins!\n')
else:
    print(f'Bot wins!\n')