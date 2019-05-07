def numMovesStones(a, b, c):
    """
    :type a: int
    :type b: int
    :type c: int
    :rtype: List[int]
    """
    list1 = [a, b, c]
    list1.sort()
    print(list1)
    max_change = (list1[2]-list1[1]-1)+list1[1]-list1[0]-1
    if max_change == 0:
        return [0, 0]
    a, b, c = list1
    min_times = 0
    while not is_true(a, b, c):
        min_times +=1
        if b-a == 1  or c-b == 1:
            min_times += 1
            break
        elif b-a >= c-b:
            a = b
            b = int((a+c)/2)
        else:
            c = b
            b = int((a+c)/2)

    return [min_times, max_change]

def is_true(a, b, c):
    if b-a == 1 and c-b == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    a, b, c = 1, 3, 7
    print(numMovesStones(4, 3, 2))
