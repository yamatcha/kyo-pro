a,b = map(int,input().split())
a-=1
if (b-1)%a == 0:
    print((b-1)//a)
else:
    print((b-1)//a+1)