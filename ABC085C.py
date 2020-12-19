N,Y = map(int,input().split())
xyz = []

for x in range(N+1):
    if len(xyz) > 0:
        break
    if (10000 * x) > Y:
        break
    for y in range(N-x+1):
        z = N - x - y
        if (10000 * x + 5000 * y + 1000 * z) == Y:
            xyz = [x,y,z]

if len(xyz) == 0:
    print("-1 -1 -1")
else:
    print(f'{xyz[0]} {xyz[1]} {xyz[2]}')
