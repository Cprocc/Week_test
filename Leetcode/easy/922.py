def sortArrayByParityII(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    odd = []
    even = []
    for i in range(len(A)):
        if A[i] % 2 == 0:
            odd.append(A[i])
        else:
            even.append(A[i])

    i = 0
    while i < (len(A)-1)/2:
        A[i*2] = odd[i]
        A[i*2 + 1] = even[i]
        i += 1

    return A



if __name__ == '__main__':
    A = [4, 2, 5, 7]
    print(sortArrayByParityII(A))
