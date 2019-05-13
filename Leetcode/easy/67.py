def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    a = int(a, 2)
    b = int(b, 2)
    res = bin(a + b)
    return res[2:]




if __name__ == '__main__':
    a = "01010"
    b = "1011"
    print(addBinary(a, b))

