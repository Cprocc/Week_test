t = int(input())

n = []
question = []
for i in range(t):
    n.append(int(input()))
    question.append(list(map(int, input().strip().split(' '))))


for i in range(t):
    res = "YES"
    a = n[i]
    temp = question[i]
    temp.sort()
    for j in range(a-2):
        if temp[j] + temp[j+2] <= temp[j+1]:
            res = 'NO'
    if temp[-2] + temp[0] <= temp[-1] or temp[-1] + temp[1] <= temp[0]:
        res = 'NO'

    print(res)
