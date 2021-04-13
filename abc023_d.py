import sys

n = int(input())
h = []
s = []
for i in range(n):
    a,b = map(int,input().split())
    h.append(a)
    s.append(b)

#与えられたheight内で全ての風船を割り切ることができるかを判定
def validate(height):
    tlimit = []
    #各風船の時間制限をまずは計算
    for j in range(n):
        #初期位置がheightを超えていたらそもそも、与えられてheight内で割れない（当たり前）
        #つまりもっと高い位置で割らないといけない
        if h[j] > height:
            #print('False')
            return False
        #x秒後の高さ height  = h+(s+x)なので、xについて解けば時間制限を計算できる
        tlimit.append( (height-h[j])/s[j] )
    #print(tlimit)
    #print(f'n = {n} max tlimit = {max(tlimit)}')
    #各時間制限がN秒以内かをチェック
    tlimit.sort()
    elasped_sec = 0
    for k in tlimit:
        if k < elasped_sec:
            #print('False')
            return False
        elasped_sec +=1

    return True

#x秒後の風船の高さ h + (s*x)
#x=nとするとペナルティは最悪 max(hi + (si*n))なのだがめんどくさいのでIntの最大値とする

left = 0
right = sys.maxsize

#2分探索を実施
ans = sys.maxsize
while abs(left-right) > 1:
    #print('----------')
    #print(f'left={left} right={right}')
    mid = (left+right) // 2
    #print(f'mid={mid}')
    #高さ=midの時に風船を割り切れるかチェック
    if validate(mid):
        right = mid
        ans = mid
    else:
        left = mid

print(ans)