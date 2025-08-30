# Function to take matrix input
def input_matrix(rows, cols, name="Matrix"):
    print(f"\nEnter elements for {name}:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Enter element {name}[{i}][{j}]: "))
            row.append(val)
        matrix.append(row)
    return matrix

# Function to pretty print a matrix
def print_matrix(matrix, name="Matrix"):
    print(f"\n{name}:")
    for row in matrix:
        print(" ".join(f"{val:5d}" for val in row))  # 5 spaces per number for alignment

# Dimensions of first matrix A
r1 = int(input("Enter number of rows for Matrix A: "))
c1 = int(input("Enter number of columns for Matrix A: "))

# Dimensions of second matrix B
r2 = int(input("Enter number of rows for Matrix B: "))
c2 = int(input("Enter number of columns for Matrix B: "))

# Check multiplication rule
if c1 != r2:
    print("Matrix multiplication not possible! (columns of A must equal rows of B)")
else:
    # Input matrices
    A = input_matrix(r1, c1, "A")
    B = input_matrix(r2, c2, "B")

    # Initialize result matrix with zeros
    C = [[0 for _ in range(c2)] for _ in range(r1)]

    # Matrix multiplication logic
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                C[i][j] += A[i][k] * B[k][j]

    # Print results
    print_matrix(A, "Matrix A")
    print_matrix(B, "Matrix B")
    print_matrix(C, "Resultant Matrix C")
