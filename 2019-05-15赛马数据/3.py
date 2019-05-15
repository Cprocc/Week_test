# 10

from sys import stdin
#
# n = int(stdin.readline().strip())
#
# start = []
# for i in range(n):
#     values = list(map(int, stdin.readline().strip().split()))
#     values = list(values)
#     start.append(values)

n = 10
start = [['.', '@', '.', '.', '.', '.', '#', '#', '@', '.'],
         ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
         ['.', '.', '.', '@', '.', '.', '#', '.', '.', '.'],
         ['#', '#', '#', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '#', '#', '.', '.', '#', '.'],
         ['.', '.', '.', '#', '#', '#', '#', '.', '.', '.'],
         ['@', '.', '.', '.', '#', '#', '.', '.', '.', '.'],
         ['#', '#', '#', '#', '#', '.', '.', '.', '.', '.'],
         ['.', '.', '#', '#', '*', '#', '#', '#', '#', '.'],
         ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

book = [[0] * n for _ in range(n)]
res = 10*100


def dfs(start_x, start_y, step):
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    if str(start[start_x][start_y]) == '@':
        global res
        if step < res:
            res = step
        return

    for go in direction:
        next_x = start_x + go[0]
        next_y = start_y + go[1]

        if next_x < 0 or next_y < 0 or next_x >= n or next_y >= n:
            continue

        if start[next_x][next_y] != "#" and book[next_x][next_y] == 0:
            book[next_x][next_y] = 1
            dfs(next_x, next_y, step+1)
            book[next_x][next_y] = 0

    return


a = b = 0
for i in range(n):
    for j in range(n):
        if start[i][j] == "*":
            a = i
            b = j
            break

book[a][b] = 1
dfs(start_x=a, start_y=b, step=0)
print(res)


