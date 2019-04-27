# 维护一个出生队列[[],[]]
n = int(input().strip())
# n = 12
res = [0]
for i in range(n):
    new_temp = []
    del_temp = 0
    for k in range(len(res)):
        res[k] += 1

    for j in range(len(res)):
        if res[j] > 2 and res[j] <8:
            new_temp.append(1)
        elif res[j] > 10:
            del_temp += 1
    res = res[del_temp:]
    res += new_temp


print(len(res))
