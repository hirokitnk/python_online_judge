while True:
    args = input()
    if int(args[0]) == 0:
        break
    total = 0
    for i in args:
        total += int(i)
    print(total)
