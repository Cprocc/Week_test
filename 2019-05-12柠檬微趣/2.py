# n = int(input().strip())
# nums = list(map(int, input().strip().split(' ')))

n = 10
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 声明一个dic{}
# 里面存储的格式为{int a:(int b, int c)}
# 表示元素a在 出现的第一个位置下表是b， 最后一个位置下标是c
# b 只在第一次访问到时更新
dic = {}
for i in range(n):
    if nums[i] not in dic.keys():
        dic[nums[i]] = (i, i)
    else:
        temp = dic[nums[i]][0]
        dic[nums[i]] = (temp, i)

# 遍历dic对每一组前后位置做减法，记录最大的
res = 0
for k in dic:
    res = max(dic[k][1] - dic[k][0], res)


print(res)
