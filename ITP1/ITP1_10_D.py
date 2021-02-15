import math

n = int(input())
xn = list(map(int,input().split(" ")))
yn = list(map(int,input().split(" ")))

d1 = 0.0
d2 = 0.0
d3 = 0.0
de = 0.0

for i in range(n):
    d1 += abs(xn[i] - yn[i])
    d2 += abs(xn[i] - yn[i]) ** 2
    d3 += abs(xn[i] - yn[i]) ** 3
    if abs(xn[i] - yn[i]) > de:
        de = abs(xn[i] - yn[i])

d2 = d2 ** (1/2)
d3 = d3 ** (1/3)

print(float(d1))
print(float(d2))
print(float(d3))
print(float(de))