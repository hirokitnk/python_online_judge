import math
while True:
    n = int(input())
    if n == 0:
        break
    list_s = list(map(float,input().split(" ")))

    m = 0
    for s in list_s:
        m += s
    m = m / n

    sd = 0
    for s in list_s:
        sd += (s-m) ** 2
    sd = math.sqrt(sd/n)

    print(sd)