a = list(map(int,input().split()))
sorted_a = sorted(a)

print(a,sorted_a)
dict_a = {}

rank = 1
for i in sorted_a:
    dict_a[i] = rank
    rank +=1

ans = []
for j in a:
    ans.append(dict_a[j])

print(ans)