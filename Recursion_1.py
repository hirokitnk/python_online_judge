#1からNまでの総和を計算する再帰関数
def func(N):
    print(f'func({N}) callled')
    if N == 0:
        return 0
    result = N + func(N-1)
    print(f'total to {N} is {result}')
    return result

print(func(5))
