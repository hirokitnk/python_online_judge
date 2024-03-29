#!/usr/bin/env python3
import sys


def solve(N: int, W: int, w: "List[int]", v: "List[int]"):
    V = sum(v)
    dp = []
    for i in range(N+1):
        dp.append( [ 10 ** 15 ] * ( V + 1 ) )
    dp[0][0]=0

    for i in range(N):
        for cur_V in range(V + 1):
            # i番目を選ばない時(選べない)
            if cur_V < v[i]:
                # cur_V(2番めのFor分の中で順番に判定したい価値の値)より、i番目の品物の重さが超えて選べない
                dp[i+1][cur_V] = dp[i][cur_V]
                #print('Not Select')
            #iを選んだ場合の価値と、選ばない場合の価値の大きい方で更新
            dp[i+1][cur_V] = min(dp[i][cur_V],dp[i][cur_V - v[i]] + w[i])    
            #print('Select')
            #print(f'i+1,cur+V,v[i],w[i]={i+1},{cur_V},{v[i]},{w[i]}')
            #for x in dp:
            #    print(x)

    #for x in dp:
    #    print(x)
    res = 0
    for j in range(V+1):
        if dp[N][j] <= W:
            res = j
    print(res)
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
