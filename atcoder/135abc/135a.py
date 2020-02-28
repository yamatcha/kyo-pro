import math
a,b = map(int,input().split())

if (b+a)%2==0:
    print(abs((b+a)//2))
else:
    print("IMPOSSIBLE")