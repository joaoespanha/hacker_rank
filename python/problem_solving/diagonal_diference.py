""" Function description
Complete the diagonal_diference  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer, , the number of rows and columns in the square matrix arr .
Each of the  next n lines describes a row, arr[i] ,and consists of n  space-separated integers arr[i][j] .

Constraints

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.
"""


def diagonalDifference(arr):
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    arry_size = len(arr) - 1

    for index, elem in enumerate(arr):
        primary_diagonal_sum += elem[index]
        secondary_diagonal_sum += elem[arry_size - index]

    return abs(primary_diagonal_sum - secondary_diagonal_sum)
