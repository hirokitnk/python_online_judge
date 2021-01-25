N = int(input())
A = list(map(int,input().split()))

B = A
tempA = []
for i in range(N,0,-1):
    #print('-----')
    #print(i)
    if i == 1:
        break

    for j in range(0,2 ** i,2):
        tempA.append(max(A [j], A[j+1] ))

    A = []
    A = tempA
    #print(A)
    tempA = []

print( B.index(min(A)) + 1 )