def clumsy(N):
    """
    :type N: int
    :rtype: int
    """
    k = N // 4
    other = N % 4
    a = [0]*N
    for i in range(1, N+1):
        a[i-1] = N+1 - i

    if N == 1:
        return a[0]
    elif N == 2:
        return a[0]*a[1]
    elif N == 3:
        return int(a[0]*a[1]/a[2])
    else:
        pass

    res = 0
    for i in range(k):
        ind = i*4
        res -= (int(a[ind]*a[ind+1]/a[ind+2]))
        res += a[ind+3]

    res += 2*(int(a[0]*a[1]/a[2]))

    if other == 1:
        res -= a[4*k]
    elif other == 2:
        res -= a[4*k]*a[4*k+1]
    elif other == 3:
        res -= int(a[4*k]*a[4*k+1]/a[4*k+2])
    else:
        pass

    return res


if __name__ == '__main__':
    a = 1
    print(clumsy(a))
