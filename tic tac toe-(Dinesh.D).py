def grid(board):
    n = len(board)
    for i in range(n):
        show_row = " | ".join(str(board[i][j]) if board[i][j] != 0 else " " for j in range(n))
        print(show_row)
        if i < n - 1:
            print("-" * (n * 4 - 3))

def check(board, n):
    for i in range(n):
        if sum(board[i]) == 15:
            return True
    for j in range(n):
        if sum(board[i][j] for i in range(n)) == 15:
            return True
    if sum(board[i][i] for i in range(n)) == 15:
        return True
    if sum(board[i][n - i - 1] for i in range(n)) == 15:
        return True
    return False

def safe_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def magic_square():
    n = safe_int_input("Enter the size of the grid: ")
    board = [[0] * n for _ in range(n)]
    player = 1

    while True:
        print(f"Player {player}'s turn:")
        r = safe_int_input("Enter row_no (0-based): ")
        c = safe_int_input("Enter col_no (0-based): ")
        num = safe_int_input("Enter the number (1-9): ")

        if 0 <= r < n and 0 <= c < n and 1 <= num <= 9 and board[r][c] == 0:
            board[r][c] = num
            grid(board)
            if check(board, n):
                grid(board)
                print(f"🎉 Player {player} wins the match!")
                break
            player = 2 if player == 1 else 1
        else:
            print("Invalid move! Try again.")

magic_square()
