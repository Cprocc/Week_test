def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
#     n应该在的位置，
# 1位1~9 共9个
# 2位10~99 共90 个
# 3位100 ~ 999 共 900个
    has = 9
    i = 1
    while True:
        n -= has
        if n <= 0:
            break
        i += 1
        bas = 9*(10**(i-1))
        has = bas * i

    res = n + has

    # res = 7111
    res -= 1
    x = int(res/i)
    r = res%i

    base = 10**(i-1)

    base += x

    return str(base)[r]




if __name__ == '__main__':
    print(findNthDigit(2147483647))