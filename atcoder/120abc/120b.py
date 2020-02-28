a,b,k = map(int,input().split(' '))
cnt=0
if a>b:
    max=a
else:
    max=b
for i in range(max,0, -1):
   # print(i)
    if (a%i==0) and (b%i==0):
        cnt+=1
    #    print(i)
    if cnt==k:
        print(i)
        break