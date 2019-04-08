def bitwiseComplement(N):
    """
    :type N: int
    :rtype: int
    """
    if N == 0:
        return 1

    def Dec2Bin(dec):
        result = ''

        if dec:
            result = Dec2Bin(dec // 2)
            return result + str(dec % 2)
        else:
            return result

    s = Dec2Bin(N)

    s1 = ""

    for i in range(len(s)):
        s1 += str(1 - int(s[i]))

    s1 = s1[::-1]

    res = 0
    for i in range(len(s1)):
        res += int(s1[i]) * int(2**i)

    return res


if __name__ == '__main__':
    N = 0
    print(bitwiseComplement(N))

