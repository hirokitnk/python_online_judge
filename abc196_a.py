a,b = map(int,input().split())
c,d = map(int,input().split())

res = max(b-c, b-d)

print(res)