# n = int(input().strip())
# nums = list(map(int, input().strip().split(' ')))

n = 6
nums = [1, 1, 2, 2, 2, 1]

dic = {}
for i in range(n):
    if nums[i] not in dic.keys():
        dic[nums[i]] = (i, i)
    else:
        temp = dic[nums[i]][0]
        dic[nums[i]] = (temp, i)

res = 0
for k in dic:
    res = max(dic[k][1] - dic[k][0], res)


print(res)
