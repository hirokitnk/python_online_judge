N,A,B = map(int,input().split())

total = 0
for i in range(N,0,-1):
    digits = str(i)
    sum_digits = 0
    #print("digits " + str(digits))
    for j in range(len(digits)):
        sum_digits += int(digits[j])
    #print("sum_digits " + str(sum_digits))
    if A <= sum_digits and sum_digits <= B:
        total += i
print(total)

#