
# 输出j：  i=[1,2]  j = 1,2
# print([j for i in [[1,2],[3,4],[5,6]] for j in i])

# def re(x):
#     xx = x
#     re_x = 0
#     while xx > 0:
#         re = xx % 10
#         xx = int(xx / 10)
#         re_x *= 10
#         re_x += re
#     if re_x == x:
#         return True
#     else:
#         return False
#
# if __name__ == '__main__':
#     x = 121
#     print(re(x))

# s = "abcd"
# a = s[1]
# print(a)

# nums = [1,8,6,2,5,4,8,3,7]
# a = 2 * sum(nums)
# a -=
# print(a)
import collections
dicts = collections.Counter('abdcdedcdsa')
for i in range(len(dicts)):
    print(dicts.most_common()[0][1])