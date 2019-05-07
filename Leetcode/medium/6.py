def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    s_len = len(s)
    n = int(s_len / 2) + 1
    m = numRows
    matrix = [[0] * n for _ in range(m)]
    if s_len <= m:
        return s
    elif m == 1:
        return s
    else:
        for j in range(n):
            if j % (m - 1) == 0:
                for i in range(m):
                    matrix[i][j] = 1
            else:
                x = j % (m - 1)
                matrix[m - x - 1][j] = 1

        k = 0
        flag = 0
        for i in range(n):
            for j in range(m):
                if matrix[j][i] == 1:
                    matrix[j][i] = s[k]
                    k += 1
                    if k == s_len:
                        flag = 1
                        break
            if flag == 1:
                break
        ss = ''
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and matrix[i][j] != 1:
                    ss += matrix[i][j]

        return ss


def convert1(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows >= len(s):
        return s

    L = [''] * numRows
    index, step = 0, 1

    for x in s:
        L[index] += x
        if index == 0:
            step = 1
        elif index == numRows -1:
            step = -1
        index += step

    return ''.join(L)


if __name__ == '__main__':
    # print(convert("ABC", 2))
    print(convert1("PAYPALISHIRING", 4))
