def isToeplitzMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    m = len(matrix)
    n = len(matrix[0])
    if m == 1 or n == 1:
        return True

    for i in range(m-1):
        cur = matrix[i][0]
        for j in range(min(n, m-i)):
            if cur != matrix[i+j][j]:
                return False

    for j in range(1, n-1):
        cur = matrix[0][j]
        for i in range(min(n-j, m)):
            if cur != matrix[i][i+j]:
                return False

    return True


if __name__ == '__main__':
    print(isToeplitzMatrix([
            [1,2,3,9],
            [5,1,2,3],
            [9,5,1,2]
    ]))
