def find_prefix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(1, n):
            matrix[i][j] += matrix[i][j - 1]
    for i in range(1, n):
        for j in range(n):
            matrix[i][j] += matrix[i - 1][j]
    return matrix

def get_submatrix_sum(prefix, i1, j1, k):
    i2 = i1 + k - 1
    j2 = j1 + k - 1

    total = prefix[i2][j2]
    if i1 > 0:
        total -= prefix[i1 - 1][j2]
    if j1 > 0:
        total -= prefix[i2][j1 - 1]
    if i1 > 0 and j1 > 0:
        total += prefix[i1 - 1][j1 - 1]
    return total

def find_max_k_submatrix(matrix, k):
    n = len(matrix)
    original = [row[:] for row in matrix]  # keep a copy to print values
    prefix = find_prefix(matrix)  # in-place modification

    max_sum = float('-inf')
    top_left = (0, 0)

    for i in range(n - k + 1):
        for j in range(n - k + 1):
            curr_sum = get_submatrix_sum(prefix, i, j, k)
            if curr_sum > max_sum:
                max_sum = curr_sum
                top_left = (i, j)

    return original, top_left, max_sum, k

def print_submatrix(matrix, i, j, k, total_sum):
    print("The maximum sub-array is:\n")
    for x in range(i, i + k):
        for y in range(j, j + k):
            print(matrix[x][y], end="  ")
        print()
    print(f"\nThe maximum sum is:\n{total_sum}")

def main():
    n = int(input("Enter the size of matrix:\n"))
    k = int(input("Enter the size of sub_array:\n"))
    matrix = [list(map(int, input().split())) for _ in range(n)]

    original, (i, j), max_sum, k = find_max_k_submatrix(matrix, k)
    print_submatrix(original, i, j, k, max_sum)

main()
