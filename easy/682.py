def calPoints(nums):
    """
    :type ops: List[str]
    :rtype: int
    """
    res = []
    for item in nums:
        if item == "C":
            res.pop()
        elif item == "D":
            res.append(res[-1] * 2)
        elif item == "+":
            res.append(res[-1]+res[-2])
        else:
            res.append(int(item))

    return sum(res)


if __name__ == '__main__':
    nums = ["5","2","C","D","+"]
    print(calPoints(nums))
