n,m,c = map(int,input().split())
b=list(map(int,input().split()))
cnt=0

for i in range(0,n):
    sum=0
    a=list(map(int,input().split()))
    for j in range(0,m):
        sum+=b[j]*a[j]
    if sum+c>0:
        cnt+=1

print(cnt)