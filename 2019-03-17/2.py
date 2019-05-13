def numPairsDivisibleBy60(time):
    """
    :type time: List[int]
    :rtype: int
    """
    for i in range(len(time)):
        time[i] = time[i] % 60

    import collections
    time = collections.Counter(time)

    times = [0]*60
    for each in time.items():
        times[each[0]] = each[1]

    count = 0
    for ind, val in enumerate(times[0:31]):
        if ind == 0 or ind == 30:
            for i in range(val):
                count += i
        else:
            if time[60-ind] != 0:
                count += times[60-ind]*val

    return count

if __name__ == '__main__':
    time = [15,63,451,213,37,209,343,319]
    print(numPairsDivisibleBy60(time))