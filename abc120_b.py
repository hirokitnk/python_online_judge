A,B,K = map(int,input().split())
div = 1
candidates = []

while A >= div and B >= div:
    if A % div == 0 and B % div ==0:
        candidates.append(div)
    div +=1

print(candidates[-1*K])