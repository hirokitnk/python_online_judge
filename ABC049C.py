import sys
sys.setrecursionlimit(100000)

S = input()
words = ["dream","dreamer","erase","eraser"]

def findMatch(nT,M):
    if nT == len(S):
        return True
    for i in words:
        t = nT
        if S[nT:].startswith(i):
            #print(str(t+len(i)))
            M = findMatch(t+len(i),M)
    return M

if findMatch(0,False):
    print("YES")
else:
    print("NO")