n = input()
n_digits = len(n)

if n_digits % 2 ==1:
    n_digits -=1

res = 0
for i in range(int((n_digits+1)/2)):
    #print(f'i={i}')
    for j in range(10 ** i,10 ** (i+1)):
        #print(f'j={j}')
        #print(str(j)+str(j))
        if int(str(j)+str(j)) > int(n):
            print(res)
            exit()
        res += 1 
print(res)