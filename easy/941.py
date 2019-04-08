def validMountainArray(A):
    """
    :type A: List[int]
    :rtype: bool
    """

    m = 0
    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            pass
        else:
            m = i-1
            break

    if m == 0 or m == len(A)-1:
        return False

    for i in range(m, len(A)-1):
        if A[i+1] >= A[i]:
            return False

    return True



if __name__ == '__main__':
    A = [1,3,3,2,1]
    print(validMountainArray(A))