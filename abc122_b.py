S = input()
c,mx = 0,0

for i in S:
    if i in ('ACGT'):
        c +=1
    else:
        mx = max(c,mx)
        c = 0

mx = max(c,mx)
print(mx)
