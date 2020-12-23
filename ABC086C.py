t,x,y = [0],[0],[0]

N = int(input())

reached = True

for i in range(1,N+1):
    args = list(map(int,input().split(" ")))
    t.append(args[0])
    x.append(args[1])
    y.append(args[2])

    deltaTime = t[i] - t[i-1]
    deltaDist = (x[i]- x[i-1]) + (y[i]-y[i-1])

    if deltaDist > deltaTime:
        reached = False

    if deltaDist % 2 != deltaTime % 2:
        reached = False

if reached:
    print("Yes")
else:
    print("No")