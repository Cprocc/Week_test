def maxUncrossedLines(s1, s2):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    m, n = len(s1), len(s2)

    matrixR = [[0] * (n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                matrixR[i][j] = matrixR[i - 1][j - 1] + 1
            else:
                matrixR[i][j] = max(matrixR[i - 1][j], matrixR[i][j - 1])
    return matrixR[m][n]


if __name__ == '__main__':
    A = [1,4,2]
    B = [1,2,4,2]
    print(maxUncrossedLines(A, B))