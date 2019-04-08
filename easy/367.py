def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    if num == 0:
        return True
    l, r = 1, num
    mid = int((l + r) / 2)
    while l <= r:
        print(mid)
        if mid * mid == num:
            return True
        elif mid * mid > num:
            r = mid
        else:
            l = mid

        new_mid = int((l+r)/2)
        if new_mid == mid:
            break
        mid = new_mid

    return False

if __name__ == '__main__':
    import time
    print(time.time())
    print(isPerfectSquare(14))
    print(time.time())