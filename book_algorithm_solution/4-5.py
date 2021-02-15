result = 0
def countUp():
    global result
    result += 1

def func(N,curNum,flag):
    if N < curNum: return
    if flag == 0b111:
        countUp()
    func(N,curNum * 10 +3, flag | (1 << 0))
    func(N,curNum * 10 +5, flag | (1 << 1))
    func(N,curNum * 10 +7, flag | (1 << 2))

def main():
    N = int(input())
    func(N,0,0)
    print(result)

main()