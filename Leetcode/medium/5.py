
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    # 反转链表-对最简单的完全一致情况进行排除
    reverse_s = s[::-1]
    if reverse_s == s:  # '' or 'a'
        return s

    else:
        long = cur = s[0]
        for i in range(1, len(s)):
            if cur in reverse_s:
                if cur == cur[::-1]:
                    # 对长度进行比较（long, cur）
                    long = max(long, cur, key=len)

                cur += s[i]
            else:
                if cur[1:] in reverse_s:  # "abcdbbfcba"
                    cur = cur[1:] + s[i]
                else:
                    cur = cur[2:] + s[i]

        # 做最后一次判断
        if cur in reverse_s:
            if cur == cur[::-1]:
                long = max(long, cur, key=len)

        return long


if __name__ == '__main__':
    s = 'abcdbbfcba'
    print(longestPalindrome(s))