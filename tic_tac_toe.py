
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
key_bindings = ['q','w','e','a','s','d','z','x','c']

def display_board(board):
    print()
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print()

def display_instructions():
    print("Welcome to Tic-Tac-Toe!")
    print("Two players ('X' and 'O') take turns to be the first to perform a full line of 3 (horizontally, vertically or diagonally).")
    print("Use the keyboard keys to pick the location of the marks, as follows:")
    display_board(key_bindings)
    print("Good luck and have fun!")
    print()

def choose_player():
    player1 = ' '
    player2 = ' '
    while player1 not in ['X','O']:
        player1 = input("Player 1: please pick a marker 'X' or 'O' :").upper()
        if player1 == 'X':
            player2 = 'O'
        elif player1 == 'O':
            player2 = 'X'
        else:
            print("Invalid input. Please pick 'X' or 'O'.")
    print(f"Player 1 will be '{player1}'.")
    print(f"Player 2 will be '{player2}'.")
    return (player1, player2)

# Checks if this position of the board has been filled already or not.
def position_filled(command):
    return board[key_bindings.index(command)] != ' '

def play_turn(current_player):
    command = ''
    valid = False
    while not valid:
        command = input(f"Player '{current_player}', place your marker :").lower()
        if command not in key_bindings:
            print("Invalid input.")
        elif position_filled(command):
            print("Position already filled.")
        else:
            valid = True
    update_board(command, current_player)
    return current_player
    
def update_board(command, current_player):
    board[key_bindings.index(command)] = current_player

def switch_players(current_player, player1, player2):
    if current_player == player1:
        return player2
    else:
        return player1

def check_winner(board, current_player):
    pos = [i for i, x in enumerate(board) if x == current_player]
    if (contains(pos, [0, 1, 2]) 
     or contains(pos, [3, 4, 5])
     or contains(pos, [6, 7, 8])
     or contains(pos, [0, 3, 6])
     or contains(pos, [1, 4, 7])
     or contains(pos, [2, 5, 8])
     or contains(pos, [3, 4, 5])
     or contains(pos, [0, 4, 8])
     or contains(pos, [2, 4, 6])):
        print(f"The winner is '{current_player}'!")
        return current_player
    elif not ' ' in board:
        print(f"Alright, I'll call it a draw!")
        return 'T'
    else:
        return None

def contains(player_positions, winning_positions):
    return all(elem in player_positions for elem in winning_positions)

def game_loop():
    player1, player2 = choose_player()
    current_player = player1
    winner = None
    display_board(board)
    current_player = play_turn(current_player)
    display_board(board)
    while (winner == None):
        current_player = switch_players(current_player, player1, player2)
        play_turn(current_player)
        display_board(board)
        winner = check_winner(board, current_player)

def play_again():
    response = None
    while response not in ['Y','N']:
        response = input("Play again? ('Y','N') :").upper()
        if response == 'Y':
            global board
            board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            return True
        elif response == 'N':
            return False
        else:
            print("Invalid input. Please pick 'Y' or 'N'.")

def play():
    display_instructions()
    playing = True
    while playing:
        game_loop()
        playing = play_again()
    print("Goodbye!")

play()
