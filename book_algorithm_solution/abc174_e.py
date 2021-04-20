n,k = int(input().split())
a = map(int,input().split())

#validate関数の実装
def validate(length):
    return True

#2分探索を実施
left = 0
right = max(a)

ans = right
while abs(left-right) > 1:
    mid = (left+right) // 2
    if validate(mid):
        right = mid
        ans = mid
    else:
        left = mid
 
print(ans)