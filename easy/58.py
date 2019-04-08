def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """

    if s == "":
        return 0
    ss = list(s)

    if len(ss) == 1 and ss[0] != '':
        return 1

    ss.reverse()
    re_s = ss


    for ind, cur in enumerate(re_s):
        if cur == " ":
            re_s = re_s[1:]
        else:
            break

    re_s.reverse()
    ss = re_s

    j = 0
    for ind, cur in enumerate(ss):
        if cur == " ":
            j = ind

    ss = ss[j+1:]
    return len(ss)


if __name__ == '__main__':
    print(lengthOfLastWord("a"))