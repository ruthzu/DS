# tic_tac_toe.py

def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print("\n")


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        try:
            move = int(input(f"Player {current_player}, choose position (1-9): "))
            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} wins!")
                break

            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"

        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")


if __name__ == "__main__":
    main()