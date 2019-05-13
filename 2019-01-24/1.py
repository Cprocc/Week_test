def canThreePartsEqualSum(A):
    """
    :type A: List[int]
    :rtype: bool
    """
    A.sort()
    print(A)


if __name__ == '__main__':
    A = [0,2,1,-6,6,-7,9,1,2,0,1]
    print(canThreePartsEqualSum(A))
