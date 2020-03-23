n,m = map(int,input().split())
sl=[]
for i in range(m):
    s =list(map(int,input().split()))
    s=s[1:]
    sl.append(s)
p = list(map(int,input().split()))

cnt=0
for i in range(2**n):
    # output=[False]*n
    flag=True
    for k in range(len(sl)):
        count=0
        for j in sl[k]:
            if((i>>(j-1))&1):
                count+=1
        if count%2!=p[k]:
            flag=False
            break
    if flag:
        cnt+=1

print(cnt)