#finding secound smallest number
#input
#3 5 6 8 3 2

nums = list(map(int,input().split()))

first_min = 999
second_min = 999

for i in nums:
    if i < first_min:
        first_min = i
        continue
    if i < second_min:
        second_min = i

print(second_min)