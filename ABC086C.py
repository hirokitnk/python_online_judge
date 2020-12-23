t[0],x[0],y[0] = 0,0,0

N = int(input())

reached = True

for i in range(N):
    t[i],x[i],y[i] = map(int,input().split())
    deltaTime = t[i] - t[i-1]
    deltaDist = (x[i]- x[i-1]) + (y[i]-y[i-1])

    if deltaDist > deltaTime:
        reached = False
        break

    if deltaDist % 2 != deltaTiem % 2:
        reached = False
        break

if reached:
    print("Yes")
else:
    print("No")