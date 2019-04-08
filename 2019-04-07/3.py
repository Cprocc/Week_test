class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        res = []

        def help(x, pattern):
            if len(x) < len(pattern):
                return False
            i = j = has = 0
            while i < len(x) and j < len(pattern):
                if x[i] == pattern[j]:
                    i += 1
                    j += 1
                    has += 1
                elif x[i].islower():
                    i += 1
                else:
                    return False
            print(x[i:], has)
            if has == len(pattern) and (x[i:].islower() or i == len(x)):
                return True
            else:
                return False

        for x in queries:
            res.append(help(x, pattern))

        return res


if __name__ == '__main__':
    Sol = Solution()
    queries = ["IXfGawluvnCa","IsXfGaxwulCa","IXfGawlqtCva","IXjfGawlmeCa","IXfGnaynwlCa","IXfGcamwelCa"]
    pattern = "IXfGawlCa"
    print(Sol.camelMatch(queries, pattern))
