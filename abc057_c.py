import math

N = input()
c = len(N)
N = int(N)

for i in range(int(math.sqrt(N)),2,-1):
    if N % i == 0:
        A = i
        B = int(N / A)
        Fvalue = max(len(str(A)),len(str(B)))
        c = min(c,Fvalue)
        #print(A,B)

print(c)