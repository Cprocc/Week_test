class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        import collections
        dic = {}
        str = str.split(' ')
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                dic[pattern[i]] = str[i]
            else:
                if dic[pattern[i]] != str[i]:
                    return False

        are = collections.Counter(dic.values())
        for item in are.values():
            if item > 1:
                return False

        return True


if __name__ == '__main__':
    Sol = Solution()
    pattern = "ababc"
    str = "dog cat dog cat cat"
    print(Sol.wordPattern(pattern, str))
    # dic = {'a':'b'}
    #     # print("a" in dic, 'b'in dic)