import math 

args = list(map(float,input().split(" ")))

a,b,C = float(args[0]),float(args[1]),args[2]

h = b * math.sin(math.radians(C))
S = a * h * 0.5

xa = a
ya = 0
xb = b * math.cos(math.radians(C))
yb = b * math.sin(math.radians(C))

L = a + b + math.sqrt((xa-xb)**2 + (ya-yb)**2)

print(float(S))
print(float(L))
print(float(h))