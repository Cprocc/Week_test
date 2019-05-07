num = list(map(int, input().strip().split(' ')))

from collections import Counter
cnum = Counter(num)

two_times = 0
one_times = 0
three_times = 3
res2 = []
res1 = []
res3 = []
for i in cnum.keys():
    if cnum[i] == 2:
        two_times += 1
        res2.append(i)
    elif cnum[i] == 1:
        one_times += 1
        res1.append(i)
    elif cnum[i] == 3:
        three_times += 1
        res3.append(i)
res1.sort()
res2.sort()

if len(res3) <= 2:
    print(0)
if two_times == 0:
    print(res1[0])
if two_times == 2:
    print(res2[0], res2[1])
