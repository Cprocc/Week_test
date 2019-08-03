n = int(input().strip())
list1 = list(map(int, input().strip().split(' ')))
temp = []
for i in range(n):
    temp.append(i)

print (n)
print (list1)

list2 = []
list2.append(temp)
list2.append(list1)
list2.sort(key=lambda x: x[1])

m = int(input().strip())
m_list = []
for i in range(m):
    m_list.append(list(map(int, input().strip().split(' '))))


for i in range(m):
    temp = 0
    for j in range(m_list[i][0]-1, m_list[i][1]):
        if list1[j] == m_list[i][2]:
            temp += 1
    print(temp)
