def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    left = 0
    res = 0
    chars = dict()  # 创建字典，用于保存字符对应的索引
    for right in range(len(s)):
        if s[right] in chars:
            left = max(left, chars[s[right]] + 1)  # left移动到right字符在字典中出现的位置的下一个位置。
        chars[s[right]] = right  # 更新s[right]的索引
        res = max(res, right - left + 1)
    return res


if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcadddd'))


