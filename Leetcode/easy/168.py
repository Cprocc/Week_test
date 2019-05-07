def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    s = ''
    while n > 0:
        a = (n-1) % 26
        temp = str(a)
        s += temp
        n = int((n-1) / 26)

    s = list(s)
    s = s[::-1]
    for i in range(len(s)):
        s[i] = chr(65 + int(s[i]))

    res = "".join(s)

    return res


if __name__ == '__main__':
    print(convertToTitle(677))
