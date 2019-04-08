def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    li = []
    candidates.sort()
    if len(candidates) == 0:
        return res

    combinationSumHelp(res, li, candidates, target, 0)

    return res


def combinationSumHelp(res, li, candidates, target, start):
    if target < 0:
        return False

    elif target == 0:
        temp = li.copy()
        res.append(temp)
        return False

    else:
        for i in range(start, len(candidates)):
            li.append(candidates[i])
            flag = combinationSumHelp(res, li, candidates, target-candidates[i], i)
            li.pop()

            if not flag:
                break

    return True


if __name__ == '__main__':
    candidates = [8, 7, 4, 3]
    target = 11
    print(combinationSum(candidates, target))
