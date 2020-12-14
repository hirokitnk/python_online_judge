n = int(input())

t_point = 0
h_point = 0

for i in range(n):
    cards = list(map(str,input().split(" ")))

    t_card = str(cards[0])
    h_card = str(cards[1])

    if t_card > h_card:
        t_point += 3
    elif t_card == h_card:
        t_point += 1
        h_point += 1 
    else:
        h_point += 3

print(t_point, h_point)