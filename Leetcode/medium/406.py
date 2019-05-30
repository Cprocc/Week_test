class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: x[1])
        people.sort(key=lambda x: x[0], reverse=True)
        res = []
        print(people)

        for i in range(len(people)):
            if i == 0:
                res.append(people[1])
            else:
                res.insert(people[i][1], people[i])
        return res


if __name__ == '__main__':
    Sol = Solution()
    print(Sol.reconstructQueue(([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]])))
