N,K = map(int, input().split())
num = list(map(int, input().strip().split(' ')))

def checkInterval(possible, sumvalue):
    startMax = N-possible
    for start in range(0,startMax + 1):
        end = start + possible
        if sum(num[start:end]) >= sumvalue:
            return True
    return False


if 1 not in num:
    print(K)

elif K >= N-1:
    print(N)

else:
    maxleng = 0
    tempmaxleng = 0
    for i in num:
        if i==1:
            tempmaxleng += 1
        else:
            if tempmaxleng > maxleng:
                maxleng = tempmaxleng
            tempmaxleng = 0
    sumvalue = maxleng
    possible = sumvalue + K

    while True:
        if not checkInterval(possible, sumvalue):
            break
        sumvalue += 1
        possible += 1
    print(possible-1)
