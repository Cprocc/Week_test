def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    res = int(dividend / divisor)
    if res >= 0:
        return res
    elif ((dividend / divisor) % 1 == 0):
        return res
    else:
        return res + 1

if __name__ == '__main__':
    print(divide(7, -2))