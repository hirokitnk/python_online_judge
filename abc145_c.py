import itertools
import math

#変数格納
N = int(input())
cities = {}
for i in range(N):
    cities[str(i)] = list(map(int,input().split()))

#各都市間の距離を計算して配列に格納
two_cities_combi = list(map(''.join,itertools.permutations(cities,2)))
cities_distance = {}
for i in two_cities_combi:
    c1,c2 = cities[i[0]],cities[i[1]]
    cities_distance[str(i)] = ( math.sqrt( (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 ) ) 

#itertoolsで都市の組み合わせを求め距離を計算する
cities_routes = list(map(''.join,itertools.permutations(cities)))

total_distances =[]
for route in cities_routes:
    distance = 0
    for k in range(len(route)-1):
        distance += cities_distance[ route[k:k+2] ]
        
    total_distances.append(distance)

print(sum(total_distances)/len(total_distances))