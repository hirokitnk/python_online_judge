n,k = map(int,input().split())

def g1(arg):
    nums = []
    for i in str(arg):
        nums.append(int(i))
    nums.sort(reverse=True)
    return int(''.join(map(str,nums)))

def g2(arg):
    nums = []
    for i in str(arg):
        nums.append(int(i))
    nums.sort()
    return int(''.join(map(str,nums)))

x = n
for i in range(k):
    x = g1(x) - g2(x)

print(x)