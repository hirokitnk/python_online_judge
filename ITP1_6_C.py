buildings = [[[0 for i in range(10)] \
    for i in range(3)] \
    for i in range(4)]

n = int(input())

for ii in range(n):
    tenant = list(map(int,input().split(" ")))
    buildings[tenant[0]-1][tenant[1]-1][tenant[2]-1] += tenant[3]

separator = 0

for bb in buildings:
    for ff in bb:
        result = ""
        for rr in ff:
            result += " " + str(rr)
        print(result)
    separator += 1
    if separator < 4:
        print("####################")