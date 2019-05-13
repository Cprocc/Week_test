def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] not in vowels:
            l += 1
        elif s[r] not in vowels:
            r -= 1
        else:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
    return "".join(s)

if __name__ == '__main__':
    s = 'leetcode'
    s = list(s)
    print(s)
    print(reverseVowels(s))
