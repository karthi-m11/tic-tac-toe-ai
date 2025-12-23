# Tic-Tac-Toe AI (Minimax) - Internship Task

# Create empty board
board = [" " for _ in range(9)]

# Display the board
def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Check for winner
def check_winner(player):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False

# Check for draw
def is_draw():
    return " " not in board

# Minimax algorithm
def minimax(ai_turn):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if ai_turn:
        best = -10
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                if score > best:
                    best = score
        return best
    else:
        best = 10
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                if score < best:
                    best = score
        return best

# AI move
def ai_move():
    best_score = -10
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Show board positions guide
def show_positions():
    print("Board positions are numbered 0-8 like this:")
    print("0 | 1 | 2")
    print("--+---+--")
    print("3 | 4 | 5")
    print("--+---+--")
    print("6 | 7 | 8\n")

# Main game
print("WELCOME TO TIC-TAC-TOE!")
print("You are X | AI is O")
print("Good luck!\n")

show_positions()

while True:
    show_board()
    try:
        user_pos = int(input("Enter your move (0-8): "))
    except ValueError:
        print("Please enter a valid number between 0 and 8.")
        continue

    if user_pos < 0 or user_pos > 8 or board[user_pos] != " ":
        print("Invalid move, try again.")
        continue

    board[user_pos] = "X"

    if check_winner("X"):
        show_board()
        print("🎉 Congratulations! You won!")
        break

    if is_draw():
        show_board()
        print("🤝 It's a draw!")
        break

    ai_move()

    if check_winner("O"):
        show_board()
        print("😔 AI wins! Better luck next time.")
        break

    if is_draw():
        show_board()
        print("🤝 It's a draw!")
        break

# Keep terminal open (for double-click run)
input("\nPress Enter to exit...")

Follow the instructions on screen to play the game.

## Learning Outcomes
- Implemented a simple AI using the Minimax algorithm  
- Learned basic game logic and decision-making  
- Practiced handling user input and interactive terminal games

## Author
Karthi Karthik

