size = list(map(int,input().split(" ")))

n_row = size[0]
n_col = size[1]

table =[]
for i in range(n_row):
    table.append(list(map(int,input().split(" "))))

for i in range(n_row):
    sum_col = 0
    for j in range(n_col):
        sum_col += table[i][j]
    table[i].append(sum_col)

sum_rows = []
for i in range(n_col+1):
    sum_row = 0
    for j in range(n_row):
        sum_row += table[j][i]
    sum_rows.append(sum_row)

table.append(sum_rows)

for row in table:
    print(' '.join(list(map(str,row))))
