# def groupAnagrams(s):
#     dic = {}
#     re = []
#     i = 0
#     for item in s:
#         temp0 = item
#         temp = sorted(list(item))
#         if str(temp) not in dic:
#             dic[str(temp)] = i
#             i += 1
#
#         re[dic[str(temp)]].append(str(temp0))
#
#
#     print(re)


def groupAnagrams(strs):
    d = {}
    for w in sorted(strs):
        key = tuple(sorted(w))
        print(d.get(key, []))
        d[key] = d.get(key, []) + [w]
        print(d[key])
    return list(d.values())


if __name__ == '__main__':
    s = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(s))