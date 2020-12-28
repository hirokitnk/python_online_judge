N = int(input())
num = 0
k = 0

for i in range(N,0,-1):
    if i % 2 == 0:
        continue
    for j in range(i,0,-1):
        if i % j == 0:
            k += 1
    if k == 8:
        num += 1
    k = 0

print(num) 