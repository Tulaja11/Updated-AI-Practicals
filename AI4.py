def print_solution(board, N):
    for i in range(N):
        row = ['Q' if board[i] == j else '.' for j in range(N)]
        print(" ".join(row))
    print("\n")

def solve_n_queens(N):
    def is_safe(row, col):
        return not cols[col] and not diag1[row - col] and not diag2[row + col]

    def place_queen(row):
        if row == N:
            print("Solution:")
            print_solution(board, N)
            return True  

        for col in range(N):
            if is_safe(row, col):
                board[row] = col
                cols[col] = diag1[row - col] = diag2[row + col] = True
                if place_queen(row + 1):
                    return True
                cols[col] = diag1[row - col] = diag2[row + col] = False
        return False

    board = [-1] * N
    cols = [False] * N
    diag1 = {}
    diag2 = {}

    for i in range(-N, N):
        diag1[i] = False
    for i in range(2 * N):
        diag2[i] = False

    if not place_queen(0):
        print("No solution exists for N =", N)

N = int(input("Enter the value of N for N-Queens problem: "))
solve_n_queens(N)
