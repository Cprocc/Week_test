def transpose(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    matrix = [[0]*len(A) for _ in range(len(A[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = A[j][i]

    return matrix


if __name__ == '__main__':
    nums = [[1, 2], [4, 5], [7, 8]]
    print(transpose(nums))