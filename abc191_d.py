import math
X,Y,R = map(float,input().split())
X *= 10 **4
Y *= 10 **4
R *= 10 **4
a = int(math.ceil(X-R))
b = int(math.floor(X+R))
R2 = R **2
res = 0
for i in range(a,b+1,10**4):
    yrange = math.sqrt(R2 - (X-i)**2 )
    c = int(math.ceil(Y-yrange))
    d = int(math.floor(Y+yrange))
    if d==c :
        res +=1
    else:
        res += (d//10**4-c//10**4) +1
print(res)