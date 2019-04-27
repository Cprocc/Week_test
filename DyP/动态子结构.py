s1 = 'AB12N3B4V5A6'
s2 = '123456AA'

m, n = len(s1), len(s2)

matrixR = [[0]*n for i in range(m)]

print(matrixR)
for i in range(0, m):
    for j in range(0, n):
        if i == 0 or j == 0:
            matrixR[i][j] = 1 if (s1[i] == s2[j]) else 0
        else:
            matrixR[i][j] = max(matrixR[i-1][j-1] + 1, matrixR[i-1][j], matrixR[i][j-1]) if s1[i] == s2[j] else max(matrixR[i-1][j], matrixR[i][j-1])
        print(i, j)
print(matrixR[m-1][n-1])
