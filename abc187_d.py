N = int(input())
AB = [ list(map(int,input().split())) for _ in range(N) ]
A = [ i[0] for i in AB]
#B = [ i[1] for i in AB]
sumA = sum(A)
sumB = 0
visited = 0

AB.sort(reverse=True)
for i in AB:
    visited +=1
    sumB += (i[0] + i[1])
    sumA -= i[0]
    if sumB > sumA:
        print(visited)
        exit()