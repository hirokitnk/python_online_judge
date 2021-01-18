N = int(input())
xy_l = []
for i in range(N):
    xy = []
    A = int(input())
    xy = [list(map(int,input().split())) for _ in range(A)]
    xy_l.append(xy)
maxT = 0

# y=1 正直者 y=0 不親切
for i in range (1 << N):
    flag = False
    for j in range(N):
        if i & (1 << j):
            for k in xy_l[j]:
                if (i & (1 << k[0]-1)) >> k[0]-1 != k[1]:
                    flag = True
                    break
        #else: #不親切ものの言うことはそもそも信用できないのでチェックしない
        #    for k in xy_l[j]:
        #        if (i & (1 << k[0]-1)) >> k[0]-1 == k[1]:
        #            flag = True
        #            break
        if flag:
            break
    if not flag:
        maxT = max(maxT,bin(i).count('1'))

print(maxT)