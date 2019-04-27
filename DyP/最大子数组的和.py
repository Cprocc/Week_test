A = [-1, 0, -8, 7, 5, -4, 3, 2, 10, -9, -11]


def max_sum(A):
    sum = 0
    subsum = 0
    for i in range(len(A)):
        subsum = max(A[i], subsum + A[i])
        sum = max(sum, subsum)

    return sum

print(max_sum(A))