x = int(input())
m = int(input())

nums = []
for i in str(x):
    nums.append(int(i))
d = max(nums) + 1
ans = 0

if d ==1:
    d = 2

while True:
    if d > 36:
        break
    if int(str(x),d) > m:
        break
    ans += 1
    d += 1
print(ans)