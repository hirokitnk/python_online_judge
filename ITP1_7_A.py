while True:
    scores = list(map(int,input().split(" ")))
    m = scores[0]
    f = scores[1]
    r = scores[2]
    total = m + f
    if m == -1 and f == -1 and r == -1:
        break
    elif m == -1 or f == -1:
        print("F")
    elif total >= 80:
        print("A")
    elif total >= 65:
        print("B")
    elif total >= 50:
        print("C")
    elif total >= 30:
        if r >= 50:
            print("C")
        else:
            print("D")
    else:
        print("F")
        