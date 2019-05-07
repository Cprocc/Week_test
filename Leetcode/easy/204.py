class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime = [True] * n
        for i in range(2, n):
            if prime[i]:
                j = i * 2
                while j < n:
                    prime[j] = False
                    j += i

        count = 0

        for ind, val in enumerate(prime[2:]):
            if val == True:
                count += 1

        return count