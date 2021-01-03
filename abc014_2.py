N,X = map(int, input().split())
A = list(map(int, input().split()))
total = 0

for i in range( N ):
    if X & ( 1 << i ):
        total += A[i]

print(total)