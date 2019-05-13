def letterCasePermutation(S):
    """
    :type S: str
    :rtype: List[str]
    """
    res = []
    S = list(S)
    backtrack(S, 0, res)
    return res


def backtrack(S, i, res):
    if i == len(S):
        temp = ''.join(S)
        res.append(temp)
        return
    backtrack(S, i+1, res)
    if S[i].isalpha():
        if S[i].islower():
            S[i] = S[i].upper()
        else:
            S[i] = S[i].lower()
        backtrack(S, i+1, res)
        if S[i].islower():
            S[i] = S[i].upper()
        else:
            S[i] = S[i].lower()


if __name__ == '__main__':
    S = 'a1b2'
    print(letterCasePermutation(S))
