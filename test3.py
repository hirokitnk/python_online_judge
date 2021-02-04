def func(n):
    if n == 0 or n ==1:
        return 1
    res = func(n-1) + func(n-2)
    return res

print(func(5))
