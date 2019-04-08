def findJudge(N, trust):
    """
    :type N: int
    :type trust: List[List[int]]
    :rtype: int
    """
    a = [0] * N
    for i in range(len(trust)):
        a[trust[i][1]-1] += 1
    if max(a) == N - 1:
        return a.index(max(a))+1
    return -1


if __name__ == '__main__':
    N = 4
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    print(findJudge(N, trust))