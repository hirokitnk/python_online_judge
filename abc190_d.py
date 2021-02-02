N = int(input())

def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

divs = divisor(N)

i=0
ans=0
for div in divs:
    #print(div)
    i+=1
    if i > len(divs) /2:
        break
    if div % 2==1:
        ans+=1

print(ans**2)
