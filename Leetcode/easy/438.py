def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    import collections
    aim_dist = collections.Counter(p)
    res = []
    count = 0
    aim_count = len(aim_dist)
    cur_dist = collections.Counter()
    for i in range(len(p)-1):
        if s[i] in aim_dist:
            cur_dist.update(s[i])
            count += cur_dist[s[i]] == aim_dist[s[i]]

    for j in range(len(s) - len(p) + 1):
        right = j + len(p) - 1
        if s[right] in aim_dist:
            cur_dist.update(s[right])
            count += cur_dist[s[right]] == aim_dist[s[right]]

        if count == aim_count:
            res.append(j)

        if s[j] in aim_dist:
            flag = 1
            if cur_dist[s[j]] == aim_dist[s[j]]:
                flag = 0

            cur_dist.subtract(s[j])
            count -= flag == 0

    return res


if __name__ == '__main__':
    s = "baa"
    p = "aa"
    print(findAnagrams(s, p))
