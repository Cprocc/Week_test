class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ptr2 = ptr3 = ptr5 = 0
        if n == 0: return
        if n == 1: return 1

        k = [1]
        for i in range(1, n):
            cur = min(k[ptr2] * 2, k[ptr3] * 3, k[ptr5] * 5)
            if cur == k[ptr2] * 2:
                ptr2 += 1
            if cur == k[ptr3] * 3:
                ptr3 += 1
            if cur == k[ptr5] * 5:
                ptr5 += 1

            k.append(cur)

        # print(k)
        return k[-1]


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.nthUglyNumber(10))
