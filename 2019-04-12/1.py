from sys import stdin
# n = int(input().strip())
# star, aim = list(map(str, input().strip().split(',')))
# res = []
# while True:
#     te = list(map(str, input().strip().split(',')))
#     if te == ['']:
#         break
#     else:
#         res.append(te)

star = 'A'
aim = 'F'
res = [
       ['B', 'A'],
       ['D', 'B'],
       ['F', 'B'],
       ['E', 'A'],
       ['F', 'E'],
       ['E', 'D'],
       ['D', 'B'],
       ['C', 'B']]

list_per = []
list_aim = []
for i in range(len(res)):
    list_per += res[i][1]
    list_aim += res[i][0]

cur = set()
end = set()
cur.add(star)
flag = 0
times = 0
for j in range(len(cur)):
    item = list(cur)[j]
    for i in range(len(list_per)):
        if list_per[i] in cur:
            end.add(list_aim[i])
    times += 1
    if aim in end:
        flag = 1
        break
    cur = end
    end = set()
    if times >= len(list_aim):
        flag = 0
        break

print(times)
