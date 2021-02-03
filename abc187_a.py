A,B = input().split()
sumA,sumB = 0,0

for i in range(len(A)):
    sumA += int(A[i])
for i in range(len(B)):
    sumB += int(B[i])

if sumA >= sumB:
    print(sumA)
else:
    print(sumB)