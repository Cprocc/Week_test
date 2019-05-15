from sys import stdin
n, m, k = map(int, stdin.readline().strip().split())

start = []
for i in range(m):
    values = list(map(int, stdin.readline().strip().split()))
    start.append(values)
start.append([k, 1])


# m, n = 2, 2+1
# start = [[6, 2], [13, 3], [5, 1]]
# start.sort(key=lambda x: x[1]/x[0], reverse=True)
# print(start)

n += 1
ans = 0

def dfs(ans, n):
    if n <= 0:
        return ans
    else:
        temp = []
        for i in range(len(start)):
            temp.append(dfs(ans+start[i][0], n - start[i][1]))

    return min(temp)

print(dfs(ans, n))

