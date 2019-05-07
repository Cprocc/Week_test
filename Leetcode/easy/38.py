class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cur_str = '1'
        cur_time = 1
        res = ''
        while cur_time < n:
            cur_index = 0
            while cur_index < len(cur_str):
                temp_time = self.sub_time(cur_str[cur_index:])
                res += str(temp_time)
                res += str(cur_str[cur_index])

                cur_index += temp_time
            cur_time += 1
            cur_str = res
            res = ""
        return cur_str

    def sub_time(self, s):
        times = 1
        for i in range(1, len(s)):
            if int(s[i]) == int(s[i-1]):
                times += 1
            else:
                break
        return times


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.countAndSay(1))
