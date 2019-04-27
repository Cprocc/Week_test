m = list(map(int, input().strip().split(' ')))
n, max_water = m

m1 = list(map(int, input().strip().split(' ')))
contain = m1

contain.sort()
print(contain)

# 计x为男生的倒水数量
x = contain[n] if contain[n] < 2*contain[0] else 2*contain[0]

res = 1.5*n*x if 1.5*n*x < max_water else max_water

print('%6f' % res)
