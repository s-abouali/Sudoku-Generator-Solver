import random

SIZE = 9


def print_board(board):
    for i in range(SIZE):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(SIZE):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            print(board[i][j], end=" ")
        print()


def is_valid(board, row, col, num):
    for x in range(SIZE):
        if board[row][x] == num:
            return False

    for x in range(SIZE):
        if board[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve(board):
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)

                for num in numbers:
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve(board):
                            return True

                        board[row][col] = 0

                return False

    return True


def create_full_board():
    board = [[0] * SIZE for _ in range(SIZE)]
    solve(board)
    return board


def create_puzzle(board, blanks=40):
    puzzle = [row[:] for row in board]

    removed = 0

    while removed < blanks:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            removed += 1

    return puzzle


def user_solve(puzzle):
    while True:
        print("\nCurrent Puzzle:\n")
        print_board(puzzle)

        print("\n1. Fill a Cell")
        print("2. Solve Puzzle")
        print("3. Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            row = int(input("Row (1-9): ")) - 1
            col = int(input("Column (1-9): ")) - 1
            num = int(input("Number (1-9): "))

            if puzzle[row][col] != 0:
                print("Cell already filled.")
            elif is_valid(puzzle, row, col, num):
                puzzle[row][col] = num
            else:
                print("Invalid move.")

        elif choice == "2":
            solution = [r[:] for r in puzzle]

            if solve(solution):
                print("\nSolved Puzzle:\n")
                print_board(solution)
            else:
                print("No solution exists.")

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


print("=" * 35)
print("     SUDOKU GENERATOR & SOLVER")
print("=" * 35)

complete_board = create_full_board()
puzzle = create_puzzle(complete_board, blanks=40)

user_solve(puzzle)