H,W = map(int,input().split())
S = []
for _ in range(H):
    S.append(input())
n=0
start_point = (0,0)
for i in range(1,H-1):
    s = S[i]
    if n > 0 and n != H:
        print(s)
        for j in range(1,W-1):
            print(s[j])
            if s[j] == "#":
                start_point= (i,j)
    n += 1

