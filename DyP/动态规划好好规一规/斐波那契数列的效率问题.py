import time


# 递归的效率如何
def fib_re(i):
    if i == 1:
        return 1
    elif i == 0:
        return 0
    else:
        return fib_re(i-1) + fib_re(i-2)


# 不用递归
def fib_no_re(j):
    per0 = 0
    per1 = 1
    res = 0
    if j == 0:
        return 0
    if j == 1:
        return per0
    for cur in range(2, j+1):
        res = per0 + per1
        per0 = per1
        per1 = res

    return res


# start = time.clock()
# print(fib_re(20))
# end1 = time.clock()
# print(fib_no_re(20))
# end2 = time.clock()
#
# print(end1 - start)
# print(end2 - end1)
# 6765
# 6765
# 0.0022283
# 8.6000000000001e-06


