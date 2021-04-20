import bisect
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
a.sort()
c.sort()

ans = 0
for j in b:
    a_right = bisect.bisect_right(a,j-1) 
    c_left = bisect.bisect_left(c,j+1)
    ans += (a_right) * (n - c_left)

print(ans)