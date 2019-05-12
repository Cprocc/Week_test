# s = input().strip()

s = 'XWAAAYZ'

dic = {}
flag = 1
for i in range(len(s)):
    if s[i] not in dic:
        dic[s[i]] = i
    else:
        if dic[s[i]] == i-1:
            dic[s[i]] = i
            continue
        else:
            flag = 0
            break

print(bool(flag))
