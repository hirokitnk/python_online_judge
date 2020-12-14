while True:
    args = input()
    if args[0] == "-":break
    deck = args
    m = int(input())
    for i in range(m):
        h = int(input())
        deck = deck[h:] + deck[0:h]
    print(deck)
    
