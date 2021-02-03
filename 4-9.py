def func(N,W,A):
    if N == 0:
        return W == 0
    #An-1を選ばない時
    print(N-1,W,A[:N-1])
    if func(N-1,W,A[:N-1]):
        return True
    #An-1を選ばない時
    print(N-1,W-A[N-1],A[:N-1])
    if func(N-1,W-A[N-1],A[:N-1]):
        return True
    return False

def main():
    N = 4
    W = 16
    A = [3,2,6,5]
    print(func(N,W,A))

main()