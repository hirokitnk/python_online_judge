n = int(input())
ab = []
for i in range(n):
    ab.append(list(map(int,input().split())))

#締め切り時間でソート
ab = sorted(ab,key = lambda x: x[1])
print(ab)

elasped = 0
for j in ab:
    #print('----------')
    elasped += j[0]
    #print(elasped)
    #print(j[1])
    if elasped > j[1]:
        print('No')
        exit()

print('Yes')