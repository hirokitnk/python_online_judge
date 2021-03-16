import bisect
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
b.sort()
c.sort()
#print(a,b,c)

ans = 0
for i in a:
    b_left = bisect.bisect_left(b,i)
    for j in b[b_left:]:
        c_left = bisect.bisect_left(c,j)
        ans += n-c_left
        #print(i,j)

print(ans)