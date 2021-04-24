price = int(input())
coins = [500,100,50,10,5,1]

ans = 0
for coin in coins:
    while price + coin <= 1000:
        price += coin
        ans +=1

print(ans)