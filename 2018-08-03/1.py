def commonChars(A):
    """
    :type A: List[str]
    :rtype: List[str]
    """

    def intt(a):
        return int(ord(a)-97)

    def charr(a):
        return chr(a+97)

    sum_char_list = [[0] * 26 for _ in range(len(A))]

    for i in range(0, len(A)):
        for x in str(A[i]):
            sum_char_list[i][intt(x)] += 1

    res = []

    for i in range(26):
        flag = 0
        min_i = sum_char_list[0][i]
        for j in range(1, len(sum_char_list)):
            if sum_char_list[j][i] == 0:
                flag = 1
                break
            elif sum_char_list[j][i] < min_i:
                min_i = sum_char_list[j][i]

        if flag == 0:
            for _ in range(min_i):
                res += charr(i)
    return res


if __name__ == '__main__':
    # A = ["cool","lock","cook"]
    # print(commonChars(A))
    A = ["bella", "label", "roller"]
    print(commonChars(A))