def removeOuterParentheses(S):
    """
    :type S: str
    :rtype: str
    """
    res = ""
    ans = ""
    cur_stacks = []
    for i in range(len(S)):
        ans += S[i]
        if S[i] == "(":
            cur_stacks.append('(')
        else:
            cur_stacks.pop()
            if cur_stacks == []:
                res += ans[1:-1]
                ans = ""

    return res


if __name__ == '__main__':
    S = "(()())(())(()(()))"
    print(removeOuterParentheses(S))
