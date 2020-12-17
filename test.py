n = int(input())
list_a = list(map(int,input().split(" ")))

def div2(args):
    return (args / 2)

num_div = 0
isOdd = False

while True:
    for i in list_a:
        if int(i % 2) == 1:
            isOdd = True
    if isOdd:
        break
    num_div += 1
    list_a = list(map(div2,list_a))

print(num_div)
