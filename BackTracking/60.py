class Solution:
    def getPermutation(self, n, k):
        # 首先我们的基础元素序列是
        ans = []
        nums = [str(i) for i in range(1, n+1)]
        # 我们确定第一个元素应该在的位置:
        res = 1
        depart = n
        # 计算n的阶乘
        for i in range(1, n+1):
            res *= i

        for _ in range(n):

            res = res/depart

            depart = depart-1

            pos = int(k / res) # pos的取值范围是0,n-1
            if k % res == 0:
                pos -= 1
                k = res
            else:
                k = k % res
            ans.append(nums[pos])
            nums = nums[:pos] + nums[pos+1:]

        return ''.join(ans)


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.getPermutation(4,9))