import sys
sys.setrecursionlimit(100000)

S = input()
words = ["dream","dreamer","erase","eraser"]

def findMatch(T,M):
    if T == S:
        return True
    for i in words:
        t = T
        if S.startswith(t + i):
            M = findMatch(t+i,M)
    return M

if findMatch("",False):
    print("YES")
else:
    print("NO")