def matrix(m, n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter element [{i}][{j}]: "))
            row.append(inp)
        o.append(row)
    return o


def sum(A, B):
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output


# helper to print matrices nicely
def print_matrix(mat):
    for row in mat:
        print(" ".join(map(str, row)))


m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

print("Enter Matrix A")
A = matrix(m, n)

print("Enter Matrix B")
B = matrix(m, n)

s = sum(A, B)

print("\nMatrix A:")
print_matrix(A)

print("\nMatrix B:")
print_matrix(B)

print("\nSum of matrices:")
print_matrix(s)
