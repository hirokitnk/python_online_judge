#T0=0
#T1=0
#T2=1
#TN = T(N-1) + T(N-2) + T(N-3)

def func(N):
    if N == 0 or N == 1:
        return 0
    elif N == 2:
        return 1
    return func(N-1) + func(N-2) + func(N-3)

def main(N):
    if N < 3:
        return 0
    print(func(N))

if __name__ == '__main__':
    main(10)