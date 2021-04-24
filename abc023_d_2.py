import numpy as np

n = int(input())
h = []
s = []
for i in range(n):
    a,b = map(int,input().split())
    h.append(a)
    s.append(b)

harray = np.array(h)
sarray = np.array(s)

ans = 0

for i in range(n):
    ans = harray.max()
    #1秒後の未来を予測して、最も高い位置にくる風船を、現時点で撃ち落とす
    plusone = harray +sarray
    maxindex = plusone.argmax()
    harray　＝ np.delete(harray,maxindex)
    sarray = np.delete(sarray,maxindex)
    harray += sarray

print(ans)