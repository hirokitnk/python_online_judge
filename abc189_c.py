import itertools

N = int(input())
A = list(map(int,input().split()))
result = 0

for i in itertools.combinations(range(N+1),2):
    l,r = i[0],i[1]
    x = min(A[l:r])
    result = max(result, x * (r-l))

print(result)