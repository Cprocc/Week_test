def longestCommonPrefix(strs):
    if not strs:
        return ""
    # shortest定义为strs中最短的元素
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]

    return shortest


if __name__ == '__main__':
    strs = ["aflower", "bflowtztt", "cfloighttztt"]
    res = longestCommonPrefix(strs)
    print(res)