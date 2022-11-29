# x-0 game

field = []

plr1 = 'X'
plr2 = '0'

# Set-up a play filed 3x3
for i in range (3):
    field_in = []
    for j in range (3):
        field_in.append('_')
    field.append(field_in)

def print_field(list): # Print the field 
    for i in range(3):
        print('  '.join(list[i]))

def player_move(n): # Function for players moves
        try:
            print(f'\nPlayer {n} move\n')
            move1 = input('Enter your move using COMA(,): ')
            move1_split = move1.split(',')
            x = int(move1_split[0])
            y = int(move1_split[1])
            if n == 1:
                if field[x][y] != 'X' and field[x][y] != '0': # Check if the cell is free
                    field[x][y] = 'X'
                    print()
                    print_field(field)
                else:
                    print('\nThe cell is occuped. Choose another cell')
                    player_move(n)
            elif n == 2:
                if field[x][y] != 'X' and field[x][y] != '0': # Check if the cell is free
                    field[x][y] = '0'
                    print()
                    print_field(field)
                else:
                    print('\nThe cell is occuped. Choose another cell')
                    player_move(n)
        except ValueError: # Exception of wrog symbols
            print('\nWRONG ENTER! Enter values from 0 to 2 separated by COMA(,): exmp. 0,1 or 2,2')
            player_move(n)
        except IndexError: # Exception of wrong values
             print('\nWRONG ENTER! Enter values from 0 to 2 separated by COMA(,): exmp. 0,1 or 2,2')
             player_move(n)   

def winner_check(win_list, plr_str): # Function to check for winner basing on comparison of current field with list of winning combinations
    status = False
    counter_win = 0
    win_coord = [[win_list[0][0], win_list[0][1], win_list[0][2]], [win_list[1][0], win_list[1][1], win_list[1][2]], [win_list[2][0], win_list[2][1], win_list[2][2]], # Lines
                    [win_list[0][0],win_list[1][0], win_list[2][0]], [win_list[0][1], win_list[1][1], win_list[2][1]], [win_list[0][2], win_list[1][2], win_list[2][2]], # Columns
                        [win_list[0][0], win_list[1][1], win_list[2][2]], [win_list[0][2], win_list[1][1], win_list[2][0]]] # Diags
    for i in range(len(win_coord)):
        for j in range(len(win_coord[i])):
                if plr_str == win_coord[i][0] and plr_str == win_coord[i][1] and plr_str == win_coord[i][2]:
                    counter_win += 1
    if counter_win == 3:
        status = True
        return status
    else:
        return status

game = False
counter = 0
plr_id = 0 # Player ID for GAME OVER message
a = 1 # Mark of Player1 or Player2
while counter < 9:
    if game != True:
        if a == 1:
            player_move(a)
            game = winner_check(field, plr1)
            counter += 1
            plr_id = a
            a += 1
        elif a == 2:
            player_move(a)
            game = winner_check(field, plr2)
            counter += 1
            plr_id = a
            a = 1
    else:
        print(f'\nGAME OVER!\n\nPlayer_{plr_id} wins\n') # GAME OVER message
        exit()
else:
    print(f'\nMoves over!\n\nDraw\n')