import math
n = int(input())

def judge(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    return count

ans=0
for i in range(3,n+1,2):
    if judge(i)==8:
        ans+=1

print(ans)

