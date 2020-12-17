n = int(input())
cards = list(map(int,input().split()))

list.sort(cards,reverse=True)

alice = [ cards[x] for x in range(n) if x % 2 ==0 ]
bob   = [ cards[y] for y in range(n) if y % 2 ==1 ]

print(sum(alice)-sum(bob))