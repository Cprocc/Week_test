def twoCitySchedCost(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    depart = [[0] * 2 for i in range(len(costs))]
    print(depart)
    for i in range(len(costs)):
        depart[i][0] = i
    for i in range(len(costs)):
        # 这时候应该选1
        depart[i][1] = costs[i][0] - costs[i][1]

    depart.sort(key=lambda x: x[1])

    result = []
    for i in range(len(costs)//2):
        result.append(depart[i][0])

    res = 0
    for i in range(len(costs)):
        if i not in result:
            res += costs[i][1]
        else:
            res += costs[i][0]

    return res

if __name__ == '__main__':
    twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])