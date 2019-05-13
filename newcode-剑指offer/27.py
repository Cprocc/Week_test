def MoreThanHalfNum_Solution(numbers):
    # write code here
    dic = {}
    res = 0
    ans = 0
    for index, num in enumerate(numbers):
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
        if dic[num] > res:
            res = dic[num]
            ans = num

    if res > (len(numbers) / 2):
        return ans
    else:
        return 0


print(MoreThanHalfNum_Solution([2,2,2,2,2,1,3,4,5]))