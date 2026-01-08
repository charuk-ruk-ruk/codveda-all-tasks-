def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, N):
    # base case: If all queens are placed then return true
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solve_n_queens_util(board, col + 1, N):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution
            # then remove queen from board[i][col]
            board[i][col] = 0

    # if the queen can not be placed in any row in this colum fn  return false
    return False

def print_solution(board, N, file=None):
    for i in range(N):
        row_str = ""
        for j in range(N):
            row_str += "Q " if board[i][j] == 1 else ". "
        print(row_str)
        if file:
            file.write(row_str + "\n")

def solve_n_queens(N=8, file=None):
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_n_queens_util(board, 0, N):
        msg = "Solution does not exist"
        print(msg)
        if file:
            file.write(msg + "\n")
        return False

    print_solution(board, N, file)
    return True

if __name__ == "__main__":
    try:
        N = int(input("Enter the number of queens (N): "))
        
        with open("n_queens_output.txt", "w") as f:
            msg = "-" * 20
            print(msg)
            f.write(msg + "\n")
            
            msg = f"N-Queens Solution for N={N}:"
            print(msg)
            f.write(msg + "\n")
            
            solve_n_queens(N, f)
            
            msg = "-" * 20
            print(msg)
            f.write(msg + "\n")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
