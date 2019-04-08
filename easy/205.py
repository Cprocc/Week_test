class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = []
        s2 = []
        for i in range(len(s)):
            if s[i] not in s1 and t[i] not in s2:
                s1.append(s[i])
                s2.append(t[i])
            elif s[i] in s1:
                if s2[s1.index(s[i])] != t[i]:
                    return False
            elif t[i] in s2:
                if s1[s2.index(t[i])] != s[i]:
                    return False
        return True


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.isIsomorphic('aaaaabbbbbcccccdddddeeeee','pppppqqqqqrrrrrsssssttttt'))
