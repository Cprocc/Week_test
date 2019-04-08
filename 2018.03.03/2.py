def isValid(S):
    """
    :type S: str
    :rtype: bool
    """
    while True:
        cur = S.replace('abc','')
        if cur == S:
            break
        S = cur

    if S == "":
        return True

    else:
        return False


if __name__ == '__main__':
    s = "aaabcbcbc"
    print(isValid(s))
