while True:
    args = list(map(int,input().split(" ")))
    n,x = args[0],args[1]

    if n == 0 and x == 0:
        break

    result = 0

    for i in range(1,n-1):
        for j in range(i+1,n):
            for k in range(j+1,n+1):
                #print("i+j+k=" + str(i + j + k))
                if int(i + j + k) == x:
                    #print("i+j+k=" + str(i + j + k))
                    result +=1
    print(result)