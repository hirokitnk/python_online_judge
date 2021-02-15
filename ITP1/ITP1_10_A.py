import math

position = list(map(float,input().split(" ")))

x0, x1 = position[0],position[2]
y0, y1 = position[1],position[3]

distance = math.sqrt((x1-x0)**2 + (y1-y0)**2)

print(distance)
