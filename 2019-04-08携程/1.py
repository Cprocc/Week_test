if __name__ == '__main__':
    m = list(map(str, input().strip().split(',')))
    a = {}
    flag = 0

    for item in m:
        if item not in a:
            a[item] = 1
        else:
            flag = 1

    print(flag != 0)
