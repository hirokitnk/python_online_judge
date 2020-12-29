priceA,priceB,priceC,numX,numY = map(int,input().split())

numA,numB,numC = 0,0,0

priceTotal = max(priceA,priceB,priceC) * (numX+numY)

for i in range(max(numX,numY) *2,-1,-1):
    numC = i
    numA = max(0,numX - int(numC / 2))
    numB = max(0,numY - int(numC / 2))
    priceTotal = min(priceTotal, (priceA * numA) + (priceB * numB) + (priceC * numC) )

print(priceTotal)