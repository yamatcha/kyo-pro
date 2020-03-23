a=[]
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
a3 = list(map(int,input().split()))
a=a1+a2+a3
n = int(input())
numlist=set(a)
# print(numlist)
for i in range(n):
    b = int(input())
    if b in numlist:
        for j in range(len(a)):
            if a[j]==b:
                a[j]=0
                break
# print(a)
flag=False
if a[0]==0:
    if a[3]==0 and a[6]==0:
        flag=True
    elif a[1]==0 and a[2]==0:
        flag=True
    elif a[4]==0 and a[8]==0:
        flag=True
elif a[4]==0:
    if a[3] ==0 and a[5]==0:
        flag=True
    if a[1]==0 and a[7]==0:
        flag=True
    if a[6]==0 and a[2]==0:
        flag=True
elif a[8]==0:
    if a[2]==0 and a[5]==0:
        flag=True
    if a[1]==0 and a[2]==0:
        flag=True
    
if flag:
    print("Yes")
else:
    print("No")
