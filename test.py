N = int(input())
listA, listB = [],[]

colors = {}

for i in range(N):
    a,b = map(int,input().split())
    if not a in colors:
        colors[a] = True
    elif not b in colors:
        colors[b] = True

print(len(colors)) 