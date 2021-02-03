#ユークリッドの互除法
def func(m,n):
    print(f'func({m},{n})が呼び出されました')
    r = m % n
    print(f'rの値は{r}です')
    if r == 0:
        print(f'nの値を返します{n}です')
        return n
    print('再起的に呼び出します')
    return func(n,r)

def main():
    print(func(51,15))

main()