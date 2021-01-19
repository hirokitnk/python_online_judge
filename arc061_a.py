S = input()
num_plus = len(S) - 1
formula = ''
result = 0

for i in range( 1 << num_plus ):
    formula = S[0]
    for j in range(num_plus):   
        if i & (1 << j):
            formula += "+"
        formula += S[j+1]
    result += eval(formula)

print(result)