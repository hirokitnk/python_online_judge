t = int(input())
lr = [list(map(int,input().split())) for _ in range(t)]

def func(l,r):
    res = 0
    stop_next = False
    print('start')
    for a in range(r,l+1,-1):
        print('---')
        print('a='+ str(a))
        if stop_next:
            break
        for b in range(l,r+1):
            b_index = 0
            print('b='+str(b))
            c = a-b
            print('c='+str(c))
            if c < l:
                if b_index == 0:
                    stop_next = True
                break
            b_index +=1
            if l <= c and c<= r:
                res +=1

    print('res')
    print(res)

for case in lr:
    func(case[0],case[1])
