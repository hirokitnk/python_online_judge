N = int(input())
S = input()

#abcde
#01234  len= 5

result = 0

for i in range(0,N-2):
    if S[i:i+3] == "ABC":
        result += 1

print(result)