import itertools

N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

song_combinations = list(itertools.combinations(range(M),2))

max_scores = 0
for i in song_combinations:
    scores = 0
    for j in range(N):
        scores += max( A[j][i[0]],A[j][i[1]] )
    max_scores = max(max_scores,scores)

print(max_scores)
