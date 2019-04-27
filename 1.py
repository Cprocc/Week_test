for i in range(2, 1001):
    res = 0
    for j in range(2, int(i/2)+1):
        if i % j == 0:
            res += j
    res += 1
    if res == i:
        print(res)
