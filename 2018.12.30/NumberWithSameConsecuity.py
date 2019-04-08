"""
Return all non-negative integers of length N such that the absolute difference between every two consecutive
 digits is K.

Note that every number in the answer must not have leading zeros
except for the number 0 itself. For example, 01 has one leading
zero and is invalid, but 0 is valid.

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.


N [1, 9]
K [0, 9]
"""


def numsSameConsecDiff(N, K):
    """
    :type N: int
    :type K: int
    :rtype: List[int]
    """
    # 第一位只能是从1,9开始,只有一个数字是0的单独处理
    ans = {x for x in range(1, 10)}
    for _ in range(N-1):
        ans2 = set()
        for x in ans:
            d = x % 10  # 每次都取到导数第一位的数
            if d-K >= 0:
                ans2.add(10 * x + d-K)
            if d + K <= 9:
                ans2.add(10 * x + d+K)
        ans = ans2
    if N == 1:
        ans.add(0)
    ans = list(ans)
    ans.sort()
    return list(ans)


if __name__ == '__main__':
    list_result = numsSameConsecDiff(2, 1)
    print(list_result)
