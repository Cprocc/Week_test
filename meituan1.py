from sys import stdin
from collections import Counter


m, n = map(int, stdin.readline().strip().split())
temp = []
for i in range(m):
    temp.append(list(map(int, input().strip().split(' '))))


list1 = []
list2 = []
for i in range(m):
    for j in range(n):
        if i % 2 == 0:
            if j % 2 == 0:
                list1.append(temp[i][j])
            else:
                list2.append(temp[i][j])
        else:
            if j % 2 != 0:
                list1.append(temp[i][j])
            else:
                list2.append(temp[i][j])

s1 = len(list1)
s2 = len(list2)
c1 = dict(Counter(list1))
c2 = dict(Counter(list2))

length = m*n
flag = 0
# for i in c1.keys():
#     for j in c2.keys():
#         if i == j:
#             te = min(s1 - c1[i] + s2, s2 - c2[j] + s1)
#         else:
#             te = s1 - c1[i] + s2 - c2[j]
#             flag = 1
#
#         if te < length:
#             length = te
#
#         if flag == 1:
#             break


