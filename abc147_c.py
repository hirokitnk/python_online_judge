N = int(input())
A = []
xy = []
for a in range( N ):
    temp = []
    A.append(int(input()))
    for b in range(A[a]):
        temp.append(input())
    xy.append(temp)
maxT = 0

for i in range( 1 << N):
    can = True
    for j in range( N ):
        NTF = (i & ( 1 << j)) >> j #N番目の人が正直か不正直かのフラグ

        for k in range(A[j]):
            if not can:
                break
            x,y = map(int,xy[j][k].split())

            XTF = (i & ( 1 << (x-1) )) >> (x-1)#証言内容のX番目の人が正直か不正直かのフラグ

            if NTF: # NTF = 1 なら正直者なので証言をそのまま成り立つか判定する
                if XTF != y: #1つでも矛盾したものがあれば、成り立たない
                    can = False
                    break
            else:# NTF = 0 なら不正直者ので証言を否定したものが成り立つか判定する
                if XTF == y: #１つでも証言が成り立ってしまうえば、不正直ものになれない
                    can = False
                    break
    if can:
        maxT = max(maxT,bin(i).count('1'))

print(maxT)