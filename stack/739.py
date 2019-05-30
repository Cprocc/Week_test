class Solution:
    def dailyTemperatures(self, T):
        # 用一个栈,同时要保存坐标信息
        star = []
        res = [0] * len(T)
        for x, item in enumerate(T):
            star.append([x, item])

        stack_esc = []

        for i in range(len(star)):
            if len(stack_esc) == 0:
                stack_esc.append(star[i])

            elif stack_esc[-1][1] >= star[i][1]:
                stack_esc.append(star[i])

            elif stack_esc[-1][1] < star[i][1]:
                while len(stack_esc) > 0:
                    if stack_esc[-1][1] < star[i][1]:
                        res[stack_esc[-1][0]] = star[i][0] - stack_esc[-1][0]
                        stack_esc.pop(-1)
                    else:
                        break

                stack_esc.append(star[i])

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

