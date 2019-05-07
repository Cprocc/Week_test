# 每次只记录最后一位非0值
N = int(input().strip())

# haha = N % 50
# if haha == 0:
#     N = 50
# else:
#     N = haha


def has_0(s):
    while True:
        t = s%10
        if t != 0:
            return t
        else:
            s = s/10

res = 1
for cur in range(1, N+1):
    temp = has_0(cur)
    res *= temp
    res = has_0(res)

print(int(res))

# for j in range(len(res)):
#     if res[len(res)-1-j] != '0':
#         print(int(res[len(res)-1-j]))
#         break
