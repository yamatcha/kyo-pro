while True:
    h,w = map(int,input().split())
    if h==0 and w==0:
        break
    for i in range(1,h+1):
        for j in range(1,w+1):
            if (i%2==1 and j%2==1) or (i%2==0 and j%2==0):
                print("#",end="")
            else:
                print(".",end="")
        print()
    print()