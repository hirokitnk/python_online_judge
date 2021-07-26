#!/usr/bin/env python3
import sys


def solve(N: int, W: int, w: "List[int]", v: "List[int]"):
    dp = []
    for i in range(N+1):
        dp.append([0]*(W+1))

    for i in range(N):
        for cur_W in range(W+1):
            # i番目を選ばない時(選べない)
            if cur_W < w[i]:
                # cur_Wつまり仮の重さ限界を、その品物の重さが超えてればそもそも選べない
                dp[i+1][cur_W] = max(dp[i+1][cur_W],dp[i][cur_W])
                print('Not Select')
            else:#その品物単品で選んだ場合？
                dp[i+1][cur_W] = max(dp[i][cur_W],dp[i][cur_W - w[i]] + v[i])
                #iを選んだ場合の価値と、選ばない場合の価値の大きい方で更新
                print('Select')
            print(f'i+1,cur+W,w[i],v[i]={i+1},{cur_W},{w[i]},{v[i]}')
            for x in dp:
                print(x)

    print(dp[N][W])    
    return


# Generated by 2.4.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    w = [int()] * (N)  # type: "List[int]"
    v = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        w[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, W, w, v)


if __name__ == '__main__':
    main()