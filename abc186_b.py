H,W = map(int,input().split())

A = []
min_A = 100
for i in range(H):
    row = list(map(int,input().split() ))
    min_A = min(min_A,min(row))
    A.append(row)

result = 0
for row_a in A:
    for a in row_a:
        result += (a - min_A)

print(result)