def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    import collections
    t = collections.Counter(t)
    sdict = collections.Counter()
    left = 0
    aim = len(t)
    ans = " "
    min_length = len(s)
    bingo_count = 0

    for right in range(len(s)):
        if s[right] in t:
            sdict.update(s[right])
            if t[s[right]] == sdict[s[right]]:
                bingo_count += 1

        if bingo_count < aim:
            continue

        while bingo_count >= aim:
            if right-left+1 <= min_length:
                ans = s[left: right+1]
                min_length = right - left + 1

            left_cur = s[left]
            left += 1
            if left_cur in t:
                sdict.subtract(left_cur)
                if sdict[left_cur] < t[left_cur]:
                    bingo_count -= 1

    return ans


if __name__ == '__main__':
    S = "A"
    T = "AA"
    res = minWindow(S, T)
    print(res)
