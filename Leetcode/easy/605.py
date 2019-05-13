def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    for i in range(len(flowerbed)):
        if flowerbed[i] == 1:
            if i - 1 >= 0:
                flowerbed[i - 1] = -1
            if i + 1 <= len(flowerbed) - 1:
                flowerbed[i + 1] = -1


    res = 0
    for i in range(n):
        for j in range(len(flowerbed)):
            if flowerbed[j] == 0:
                flowerbed[j] = 1
                res += 1
                if j - 1 >= 0:
                    flowerbed[j - 1] = -1
                if j + 1 <= len(flowerbed) - 1:
                    flowerbed[j + 1] = -1


    return res == n


if __name__ == '__main__':
    flowerbed = [0,0,1,0,0]
    n = 1
    print(canPlaceFlowers(flowerbed, n))
