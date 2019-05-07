def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    left = 0
    ans = 0
    import collections
    cur_windows = collections.Counter()
    for right in range(len(s)):
        cur_windows.update(s[right])

        while right - left +1 - cur_windows.most_common()[0][1] > k:
            cur_windows[s[left]] -= 1
            left += 1

        ans = max(ans, right-left+1)

    return ans



if __name__ == '__main__':
    s = 'AABABBA'
    k = 1
    print(characterReplacement(s, k))
