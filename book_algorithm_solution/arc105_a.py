cookies = list(map(int,input().split()))

for i in range(1<<4):
    eat = 0
    rest = 0
    for j in range(4):
        if i & (1 << j):
            eat += cookies[j]
        else:
            rest += cookies[j]
    if eat == rest:
        print("Yes")
        exit()

print("No")