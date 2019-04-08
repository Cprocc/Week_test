def findCircleNum(A):
    N = len(A)
    seen = set()

    def dfs(node):
        for nei, adj in enumerate(A[node]):
            if adj and nei not in seen:
                seen.add(nei)
                dfs(nei)

    ans = 0
    for i in range(N):
        if i not in seen:
            dfs(i)
            ans += 1
    return ans


if __name__ == '__main__':
    A = [[1,1,0],
         [1,1,1],
         [0,1,1]]
    print(findCircleNum(A))
