def largestSumAfterKNegations(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    sum_co = 0
    for i in range(K):
        min_i = min(A)
        for ind in range(len(A)):
            if A[ind] == min_i:
                A[ind] = -A[ind]
                break

    for i in range(len(A)):
        sum_co += A[i]

    return sum_co


if __name__ == '__main__':
    A = [3,-1,0,2]
    K = 3
    print(largestSumAfterKNegations(A,K))