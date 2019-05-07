t,k = map(int, input().split())
s = list(map(int, input().strip().split(' ')))
index = [0]

if 1 not in s:
    print(k)

elif k >= t-1:
    print(t)

else:
    for i in range(len(s)):
        if s[i] == 0:
            index.append(i + 1)
    index.append(len(s) + 1)
    gl_len = 0
    for x in range(k+1, len(index)):
        gl_len = max(gl_len, index[x]-index[x-k-1]-1)
    print(gl_len)
