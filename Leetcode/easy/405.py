def toHex(num):
    """
    :type num: int
    :rtype: str
    """
    if num < 0:
        num = num + 16 ** 8
    print(num)

    dic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

    hexx = ''
    while int(num) >= 16:
        res = int(num % 16)
        if res > 9:
            res = dic[res]
        num = int(num / 16)
        hexx = str(res) + hexx

    if num > 9:
        num = dic[num]
    hexx = str(num) + hexx

    print(hexx)


if __name__ == '__main__':
    toHex(-1)
    print(hex(-1))

    s = "Hello, my name is John"
    s = s.split()
    print(len(s))
