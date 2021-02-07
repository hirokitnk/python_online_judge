N,X = map(int,input().split())
A = list(map(int,input().split()))
a = [i for i in A if i != X]
print(*a)