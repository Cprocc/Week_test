# m = list(map(str, input().strip().split(',')))
# n = int(input().strip())

from sys import stdin
m = stdin.readline()
n = int(input().strip())
res = len(m) % n
times = int(len(m)/n)
re = []
for i in range(times):
    for j in range(n):
        re.append(m[(i+1)*3 -1 - j])


for i in range(res):
    re.append(m[len(m) - 1 - i])

print(re)
