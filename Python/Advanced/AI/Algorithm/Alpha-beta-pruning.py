import math

# Constants for game board dimensions
ROWS = 3
COLS = 3

# Constants to represent player and computer moves
PLAYER = 'O'
COMPUTER = 'X'
EMPTY = ' '

# STATE
TIE = 'T'
CONT = 'C'


def create_board():
    """Creates an empty Tic Tac Toe board."""
    board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
    return board


def print_board(board):
    """Prints the Tic Tac Toe board."""
    for i in range(ROWS):
        print('|'.join(board[i]))
        if i < ROWS - 1:
            print('-' * 5)


def end_of_move(board):
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == EMPTY:
                return False
    return True


def get_player_move(board):
    valid_move = False
    while not valid_move:
        move = input("Enter row and column coordinates (e.g. '1 2'): ")
        try:
            row, col = map(int, move.strip().split())
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
            continue
        if row < 1 or row > ROWS or col < 1 or col > COLS:
            print("Invalid move. Row and column coordinates must be between 1 and 3.")
            continue
        if board[row-1][col-1] != EMPTY:
            print("Invalid move. That space is already taken.")
            continue
        valid_move = True
    return row - 1, col - 1


def get_winner(board):
    """Returns the winner of the game, if there is one."""
    for i in range(ROWS):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    # Check for a tie
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == EMPTY:
                return CONT
    return TIE


def evaluate(board):
    """Evaluates the score of a given board state."""
    winner = get_winner(board)
    if winner == COMPUTER:
        return 1
    elif winner == PLAYER:
        return -1
    else:
        return 0    # tie


# Alpha-Beta pruning
alpha = -math.inf
beta = math.inf


def minimax(board, depth, alpha, beta, maximizing_player):
    """Returns the optimal move for the current player using the minimax algorithm with alpha-beta pruning."""
    winner = get_winner(board)
    # if winner is not CONT or depth == 5:
    if winner is not CONT:
        return evaluate(board)
    if maximizing_player:
        max_score = -math.inf
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == EMPTY:
                    board[i][j] = COMPUTER
                    score = minimax(board, depth+1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_score = max(max_score, score)
                    alpha = max(alpha, max_score)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return max_score
    else:
        min_score = math.inf
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    score = minimax(board, depth+1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_score = min(min_score, score)
                    beta = min(beta, min_score)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return min_score


def get_computer_move(board):
    """Returns the computer's move using the minimax algorithm."""
    best_score = -math.inf
    best_move = None
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == EMPTY:
                board[i][j] = COMPUTER
                score = minimax(board, 0, alpha, beta, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


def play_game():
    """Plays a game of Tic Tac Toe."""
    board = create_board()
    current_player = PLAYER
    while True:
        print_board(board)
        if current_player == PLAYER:
            row, col = get_player_move(board)
            board[row][col] = PLAYER
            winner = get_winner(board)
            if winner is not CONT:
                print_board(board)
                if winner == PLAYER:
                    print("You win!")
                else:
                    print("It's a tie!")
                break
            current_player = COMPUTER
        else:
            print("Computer's turn...")
            row, col = get_computer_move(board)
            board[row][col] = COMPUTER
            winner = get_winner(board)
            if winner is not CONT:
                print_board(board)
                if winner == COMPUTER:
                    print("Computer wins!")
                else:
                    print("It's a tie!")
                break
            current_player = PLAYER


play_game()
