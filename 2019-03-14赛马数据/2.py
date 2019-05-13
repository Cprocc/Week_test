import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    A = sys.stdin.readline().strip()
    A = list(map(int, A.split()))
    B = sys.stdin.readline().strip()
    B = list(map(int, B.split()))
    #
    # 策略
    # 循环2n次
    #
    #   如果自己没球， 或者对方中最大值大于等于自己最大值就剔除对方
    #
    #   否则就存储自己的最大值
    A.sort()
    A.reverse()
    B.sort()
    B.reverse()
    soa = sum(A)
    sob = sum(B)
    time = 2 * n
    i = 0
    for i in range(time):
        if i % 2 == 0:
            if len(A) > 0 and len(B) > 0 and B[0] >= A[0]:
                sob -= B[0]
                del B[0]
            elif len(A) < 1:
                sob -= B[0]
                del B[0]
            else:
                del A[0]

        else:
            if len(B) >= 1 and len(A) >= 1 and A[0] >= B[0]:
                soa -= A[0]
                del A[0]
            elif len(B) < 1:
                soa -= A[0]
                del A[0]
            else:
                del B[0]

    print(soa - sob)

