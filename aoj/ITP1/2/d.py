w,h,x,y,r = map(int,input().split())

if w>=x+r and h>=y+r and 0<=x-r and 0 <=y-r:
    print("Yes")
else:
    print("No")