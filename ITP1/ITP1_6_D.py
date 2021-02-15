size = list(map(int,input().split(" ")))

mtrx_a = []
for i in range(size[0]):
    mtrx_a.append(list(map(int,input().split(" "))))

vector_b = []
for j in range(size[1]):
    vector_b.append(int(input()))

result = []
for ii in range(size[0]):
    compute = 0
    for jj in range(size[1]):
        compute += mtrx_a[ii][jj] * vector_b[jj]
    result.append(compute)

for i in result:
    print(i)
