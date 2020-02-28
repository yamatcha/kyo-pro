n=int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

sum=0

for i in reversed(range(0,n)):
    if b[i]<=a[i+1]:
        sum+=b[i]
    elif b[i]<=a[i+1]+a[i]:
        sum+=b[i]
        a[i]-=b[i]-a[i+1]
    elif a[i+1]+a[i]<=b[i]:
        sum+=a[i+1]+a[i]
        a[i]=0

print(sum)