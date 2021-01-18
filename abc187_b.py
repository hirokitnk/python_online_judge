import itertools

N = int(input())
points = [list(map(int,input().split())) for _ in range(N)]
#print(points)

result = 0

for point in itertools.combinations(points,2):
    #print(point)
    i=point[0]
    j=point[1]
    
    slope = (i[1]-j[1]) / (i[0]-j[0])
    if -1 <= slope and slope <= 1:
        result += 1

print(result)