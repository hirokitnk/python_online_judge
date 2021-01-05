import itertools

N = int(input())
P = ''.join( input().split() )
Q = ''.join( input().split() ) 
initArray = ''
for i in range(1,N+1):
    initArray += str(i)

Premutationos = list(map(''.join,itertools.permutations(initArray)))

a,b = 0,0
for j, prem in enumerate(Premutationos):
    if prem == P:
        a = j+1
    if prem == Q:
        b = j+1

print(str(abs(a-b)))