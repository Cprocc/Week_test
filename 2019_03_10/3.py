def minDominoRotations(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    have_done = []
    mix = [200000]
    mix_change = 200000
    flag = 0
    for cur, val in enumerate(A):
        if val in have_done:
            pass
        else:
            exchange = 0
            flag = 0
            for i in range(len(A)):
                if A[i] == val:
                    pass
                elif B[i] == val:
                    exchange += 1
                else:
                    flag = 1
                    break
            if flag != 1 and exchange <= mix_change:
                mix_change = exchange
            elif flag == 1:

                mix_change = 200000
        have_done.append(val)
        mix.append(mix_change)

    res = min(mix)



    A,B = B,A
    have_done = []
    mix = [200000]
    mix_change = 200000
    flag = 0
    for cur, val in enumerate(A):
        if val in have_done:
            pass
        else:
            exchange = 0
            flag = 0
            for i in range(len(A)):
                if A[i] == val:
                    pass
                elif B[i] == val:
                    exchange += 1
                else:
                    flag = 1
                    break
            if flag != 1 and exchange <= mix_change:
                mix_change = exchange
            elif flag == 1:

                mix_change = 200000
        have_done.append(val)
        mix.append(mix_change)

    res1 = min(mix)

    res = min(res,res1)
    if res < 200000:
        return res
    else:
        return -1


if __name__ == '__main__':
    A = [2, 5, 5, 5, 5, 5]
    B = [5, 2, 6, 2, 3, 2]
    print(minDominoRotations(A, B))

