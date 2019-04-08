def maxDistToClosest(seats):
    """
    :type seats: List[int]
    :rtype: int
    """
    res = 0
    left = 0
    for i in range(len(seats)):
        if seats[i] != 1:
            left += 1
        else:
            break

    right = 0
    for j in range(len(seats)):
        if seats[len(seats)-1-j] != 1:
            right += 1
        else:
            break

    seats = seats[left:len(seats)-right]

    ans = 0
    for cur in range(len(seats)):
        if seats[cur] == 0:
            ans += 1
        else:
            cur_res = int(ans/2) + ans%2
            ans = 0
            if cur_res > res:
                res = cur_res

    return max(res, left, right)


if __name__ == '__main__':
    seats = [1,0,0,0,1,0,1]
    print(maxDistToClosest(seats))
