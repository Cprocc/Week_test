from sys import stdin
n = int(stdin.readline().strip())

start = []

for i in range(n):
    values = list(map(int, stdin.readline().strip().split()))
    start.append(values)

m = int(stdin.readline().strip())

question = []

for i in range(m):
    values = list(map(int, stdin.readline().strip().split()))
    question.append(values)
#
#
# print(start, question)

# m = 4
# n = 4
# start = [[1, 1], [2, 2], [3, 3], [1, 3]]
# question = [[1, 1, 2, 2], [1, 1, 3, 3], [2, 2, 3, 3], [1, 2, 2, 3]]
start.sort(key=lambda x: x[1])
start.sort(key=lambda x: x[0])


for i in range(m):
    ans = 0
    for j in range(n):
        if question[i][2] >= start[j][0]:
            if start[j][0] >= question[i][0]:
                if question[i][1] <= start[j][1] <= question[i][3] :
                        ans += 1
        else:
            break

    print(ans)






