#!/usr/bin/env python3
import sys


def solve(N: int, K: int, a: "List[int]"):
    syou = K // N
    amari = K % N

    ans = {}
    for i in a:
        ans[i] = syou
    
    for j in sorted(a):
        if amari > 0:
            ans[j] += 1
            amari -=1
        else:
            break
    for k in ans.values():
        print(k)
    return


# Generated by 2.4.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, a)

if __name__ == '__main__':
    main()