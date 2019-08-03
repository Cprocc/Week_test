# p = (which <=s - 1)n

n = int(input())
grade = list(map(float, input().strip().split(' ')))
query_time = int(input().strip())

query = []
for i in range(query_time):
    query.append(int(input())-1)

grade_sort = sorted(grade)


def search(key):
    left = 0  # 左边界
    right = n - 1  # 右边界
    while left <= right:
        mid = (left + right) // 2  # 取得中间索引
        if key > grade_sort[mid]:
            left = mid + 1
        elif key < grade_sort[mid]:
            right = mid - 1
        else:
            while True:
                if mid == right:
                    return mid
                elif grade_sort[mid] < grade_sort[mid+1]:
                    return mid
                else:
                    mid += 1


for i in range(query_time):
    res = (search(grade[query[i]]))/n*100
    print('%.6f' % res)



