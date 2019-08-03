m = list(map(int, input().strip().split(' ')))
print(m)
n, a, b, c = m

res = int(n/c) + int(int(n/c)/a)*b

print(res)

