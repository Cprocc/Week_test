def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    rowIndex += 1
    temp = [[0] * rowIndex for _ in range(rowIndex)]
    for i in range(rowIndex):
        temp[i][0] = 1
        temp[i][i] = 1

    for i in range(1, rowIndex):
        for j in range(1, i+1):
            temp[i][j] = temp[i-1][j] + temp[i-1][j-1]
    print(temp)
    return temp[rowIndex-1]


if __name__ == '__main__':
    rowIndex = 3
    print(getRow(rowIndex + 1))