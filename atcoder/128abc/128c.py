n,m = map(int,input().split())
sl=[]
for i in range(m):
    s =list(map(int,input().split()))
    s=s[1:]
    sl.append(s)
p = list(map(int,input().split()))

for i in range(2**n):
    # output=[False]*n
    count=0
    for s in sl:
        for j in s
            if((i>>j)&1)==1:
                count+=1

