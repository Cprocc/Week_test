# A = []
# import string
# S = "123a"
# # S = string.atoi(S,base = 10)
#
# # print(float(".98"))
#
#
# # a = "1234567"
# # print(a[-1])
# #
# #
# # a = 964176192
# #
# #
# # a = bin(a)
# # a = a[2:]
# # s = a[::-1]
# # print(int(s, 2))
#
# # dic = {1:2, 2:3, 3:4}
# # print(dic.get(1), max(dic.values()))
#
# # list = [1, 2, 3]
# # print(list.pop())
#
#
# #-*-coding:utf-8-*-
# def split_new(stringstr, charstr):
#     """
#     :param stringstr: 要分割的串
#     :param charstr: 按该串分割
#     :return: 返回分割后的list
#     """
#     #stringstr = stringstr
#     tempstr = []
#     lengstring = len(stringstr)#计算串的长度
#     lengchar = len(charstr)#计算分割符的长度
#     for i in range(lengstring):
#         index = stringstr.find(charstr)#找到第一个出现charstr的坐标，如果没有找到，find返回-1
#         if index == -1:
#             tempstr.append(stringstr)
#             return tempstr
#         else:
#             tempstr.append(stringstr[:index])#取第一次出现charstr(不包含charstr)的前面部分
#             stringstr = stringstr[index+lengchar:]#把第一次出现charstr(不包含charstr)的 后面部分 重新赋值给stringstr
#
# if __name__=="__main__":
#     print (split_new(" ", "A"))


# i = 0
# # flag = 1
# # while True:
# #     i += flag
# #     if i == 100:
# #         flag = -1
# #     if i == -100:
# #         flag = 1


