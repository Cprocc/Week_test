def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    odd = []
    even = []
    for i in range(len(A)):
        if A[i]%2 == 1:
            even.append(i)
        else:
            odd.append(i)

    res = []
    for i in range(len(odd)):
        res.append(A[odd[i]])
    for j in range(len(even)):
        res.append(A[even[j]])

    return res



if __name__ == '__main__':
    A = [3,1,2,4]
    print(sortArrayByParity(A))