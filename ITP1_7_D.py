size = list(map(int,input().split(" ")))
n,m,l = size[0],size[1],size[2]

mtx_a=[]
for i in range(n):
    mtx_a.append(list(map(int,input().split(" "))))
    
mtx_b=[]
for i in range(m):
    mtx_b.append(list(map(int,input().split(" "))))

#print(mtx_a)
#print(mtx_b)

mtx_c = [[0] * l for i in range(n)]
#print(mtx_c)

for i in range(n):
    #print(f'i={i}')
    for j in range(l):
        #print(f'j={j}')
        c = 0
        for k in range(m):
            #print(f'k={k}')
            c += mtx_a[i][k] * mtx_b[k][j] 
        mtx_c[i][j] = c

for i in mtx_c:
    print(' '.join(list(map(str,i))))
