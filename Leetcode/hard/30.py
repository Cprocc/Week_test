def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    res = []
    if s == '' or words == []:
        return res

    p = "".join(words)
    import collections
    aim_dist = collections.Counter(p)
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

    end = []
    step = len(words[0])
    aim_dist = collections.Counter(words)

    aim_count = len(aim_dist)

    for ind in res:
        cur_dist = collections.Counter()
        count = 0
        for k in range(len(words)):
            temp = str(s[ind + k * step: ind + (k + 1) * step])
            temp_a = [temp]

            if temp in aim_dist:
                cur_dist.update(temp_a)
                count += cur_dist[temp] == aim_dist[temp]
            else:
                break

        if count == aim_count:
            end.append(ind)

    return end


if __name__ == '__main__':
    words = ['foo','bar']
    s = 'barfoothefoobarman'
    res = findSubstring(s, words)
    print(res)