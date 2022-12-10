import random

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
        player1 = marker
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
    return player1, player2


def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, mark):
    if board[7] == board[8] == board[9] == mark:
        print(f'{mark} wins')
        return True
    elif board[4] == board[5] == board[6] == mark:
        print(f'{mark} wins')
        return True
    elif board[1] == board[2] == board[3] == mark:
        print(f'{mark} wins')
        return True
    elif board[3] == board[5] == board[7] == mark:
        print(f'{mark} wins')
        return True
    elif board[1] == board[5] == board[9] == mark:
        print(f'{mark} wins')
        return True
    elif board[1] == board[4] == board[7] == mark:
        print(f'{mark} wins')
        return True
    elif board[2] == board[5] == board[8] == mark:
        print(f'{mark} wins')
        return True
    elif board[3] == board[6] == board[9] == mark:
        print(f'{mark} wins')
        return True
    else:
        pass

def choose_first():
    first = random.randint(1, 2)
    return f'Player{first} goes first'
    pass


def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    z = True
    while z:
        if ' ' in board:
            return False
        else:
            return True


def player_choice(board):
    y = False
    while not y:
        b = input('Enter your next move (1-9): ')
        if b.isdigit():
            if int(b) in range(1, 10):
                b = int(b)
                if space_check(board, b) != ('X' or 'O'):
                    y = True
                    return b
            else:
                print("That's invalid")
        else:
            print("That's invalid")


def replay():
    z = False
    while not z:
        f = input('Another game? (Y/N): ')
        acceptable = ('Y', 'N', 'y', 'n')
        if f in acceptable:
            if f == 'Y' or f == 'y':
                print('Great!')
                return True
            else:
                return False
        else:
            print('Please answer Y or N')
            pass


#######

def move():
    o = True
    while o:
        p = player_choice(blank_board)
        if space_check(blank_board, p):
            if '1' in a:
                place_marker(blank_board, player1_marker, p)
                display_board(blank_board)
                o = False
            else:
                place_marker(blank_board, player2_marker, p)
                display_board(blank_board)
                o = False
        else:
            print('Occupied')
            pass


def move2():
    k = True
    while k:
        t = player_choice(blank_board)
        if space_check(blank_board, t):
            if '1' in a:
                place_marker(blank_board, player2_marker, t)
                display_board(blank_board)
                k = False
            else:
                place_marker(blank_board, player1_marker, t)
                display_board(blank_board)
                k = False
        else:
            print('Occupied')
            pass


game_on = True
while game_on:
    print('Welcome to Tic Tac Toe!')

    player1_marker, player2_marker = player_input()
    a = choose_first()
    print(a)

    blank_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(blank_board)
    x = True
    while x:
        # first player turn
        move()
        if win_check(blank_board, 'X'):
            if not replay():
                game_on = False
                break
            else:
                break
        if win_check(blank_board, 'O'):
            if not replay():
                game_on = False
                break
            else:
                break
        if full_board_check(blank_board):
            print('Game Over')
            if not replay():
                game_on = False
                break
            else:
                break
        #second player turn
        move2()
        if win_check(blank_board, 'X'):
            if not replay():
                game_on = False
                break
            else:
                break
        if win_check(blank_board, 'O'):
            if not replay():
                game_on = False
                break
            else:
                break
        if full_board_check(blank_board):
            print('Game Over')
            if not replay():
                game_on = False
                break
            else:
                break
        if full_board_check(blank_board):
            print('Game Over')
            if not replay():
                game_on = False
                break
            else:
                break
        else:
            pass

    pass
