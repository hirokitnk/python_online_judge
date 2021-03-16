s = input()
index = 1
for i in s:
    if index % 2 == 1:
        if i.isupper():
            print('No')
            exit()
    if index % 2 == 0:
        if i.islower():
            print('No')
            exit()
    index += 1

print('Yes')