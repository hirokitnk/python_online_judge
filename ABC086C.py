N = int(input())

def travel(t,x,y,M):
    if t == t1:
        if x == x1 and y == y1:
            #print("Reached")
            #print(t,x,y,M)
            return True
        #print(t,x,y,M)
        return
    #print(t,x,y,M)
    if M:
        return True
    M = travel(t+1,x+1,y,M)
    if M:
        return True
    M = travel(t+1,x-1,y,M)
    if M:
        return True
    M = travel(t+1,x,y+1,M)
    if M:
        return True
    M = travel(t+1,x,y-1,M)
    return M

Reached = False

for i in range(N):
    t1,x1,y1 = map(int,input().split())
    if travel(0,0,0,False):
        Reached = True
    else:
        Reached = False

if Reached:
    print("Yes")
else:
    print("No")