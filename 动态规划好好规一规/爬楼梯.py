# class Solution:
#     def jumpFloor(self, number):
#         # write code here
#         if number <= 2:
#             return number
#         else:
#             return self.jumpFloor(number - 1) + self.jumpFloor(number - 2)
#
#


number = 2


def jump(number):
    if number <= 0:
        return 0
    else:
        return pow(2, number - 1)


print(jump(number))
