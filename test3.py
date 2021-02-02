N = int(input())
P = [list(map(int,input().split())) for _ in range(N)]
P.sort()
print(P)