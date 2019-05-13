def isOneBitCharacter(bits):
    """
    :type bits: List[int]
    :rtype: bool
    """
    if bits == [0]:
        return True
    res = 0
    i = 0
    while i < len(bits)-2:
        if bits[i] == 1:
            i += 2
        else:
            i += 1

    res = i

    if res == len(bits) - 1:
        if bits[res] == 0:
            return True
        else:
            return False
    else:
        if bits[res:res + 2] == [0, 0]:
            return True
        else:
            return False


if __name__ == '__main__':
    bits = [1,1,0]
    print(isOneBitCharacter(bits))