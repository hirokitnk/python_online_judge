letter_map = {}
for i in range(26):
    letter_map[chr(97+i)] = 0

while True:
    try:
        args = input()
    except EOFError:
        break
    if args == "":
        break
    for i in args:
        if i.isalpha():
            letter_map[i.lower()] += 1

for i in letter_map:
    print(f'{i} : {letter_map[i]}')
