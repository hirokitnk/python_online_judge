n = int(input())
abc = []
for i in range(n):
    abc.append(list(map(int,input().split())))

abc = sorted(abc,key = lambda x: x[0],reverse=True)

print(abc)

#for j in abc:
