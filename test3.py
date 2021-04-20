n = int(input())

for i in range(1<<n):
    print('----------')
    print(i)
    print(bin(i))
    for j in range(n):
        print(i & (1<<j))


