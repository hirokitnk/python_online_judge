N = int(input())
A = list(map(int,input().split()))

ans = 0
while True:
    tempList = map(lambda x:x&1,A)
    if sum(tempList) > 0:
        break
    ans += 1
    A = (list(map(lambda x:int(x/2) , A)))

print(ans)