# s = input().strip()

# s = 'XWAAAYZ'
s = 'XAX'

# 声明一个空的字典
dic = {}
# 声明一个标志变量
flag = 1

# 遍历整个字符串
for i in range(len(s)):
    # 如果当前字符不在字典的key中,那么添加{s[i]:i}
    if s[i] not in dic:
        dic[s[i]] = i

    else:
        # 如果当前字符在字典的key中，
        # 判断当前的字符位置i是否和字典中存的位置dic[s[i]]相邻
        #     如果相邻字更新一下dic[s[i]]
        #     如果不相邻则不符合题意，将标志变量更改为0
        if dic[s[i]] == i-1:
            dic[s[i]] = i
        else:
            flag = 0
            break

print(bool(flag))
