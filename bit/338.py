class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num < 0:
            return []
        res = [0, 1]
        if num <= 1:
            return res[:num + 1]

        def next(cur):
            nex = cur.copy()
            for i in cur:
                nex.append(i + 1)
            return nex

        nex = [1, 2]
        wei = 2
        while wei < num + 1:
            res += nex
            cur = nex.copy()
            nex = next(cur)
            wei += len(res)

        res += nex
        return res[:num + 1]


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.countBits(15))