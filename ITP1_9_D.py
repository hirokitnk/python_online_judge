string = input()
n = int(input())

def reverse(x):
    return x[::-1]

for i in range(n):
    line = list(map(str,input().split(" ")))
    command = line[0]
    a = int(line[1])
    b = int(line[2])

    if command == "replace":
        string = string[0:a] + line[3] + string[b+1:len(string)] 
        #print("repalce:" + string)
    elif command == "reverse":
        string = string[0:a] + reverse(string[a:b+1]) + string[b+1:len(string)] 
        #print("reverse:" + string)

    elif command == "print":
        print(string[a:b+1])
        #print("print" + string)


