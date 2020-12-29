N = int(input())
S = input()
kmap = {}

for i in range(10):
    magic = S
    if str(i) in magic:
        delidxA = magic.find(str(i))
        magicA = magic[delidxA+1:]
    else:
        continue

    for j in range(10):
        magic = magicA
        if str(j) in magic:
            delidxB = magic.find(str(j))
            magicB = magic[delidxB+1:]
        else:
            continue

        for k in range(10):
            magic = magicB
            if str(k) in magic:
                kmap[str(i)+str(j)+str(k)] = True

print(len(kmap))