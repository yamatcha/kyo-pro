n,a,b = map(int,input().split())
total = 0
i = 0

def findSumofDigits(num):
    sum=0
    while num>0:
        sum+=num%10
        num//=10
    return sum

while i<=n:
    sum = findSumofDigits(i)
    if a<=sum and sum<=b:
        total+=i
#        print(sum)
    i+=1

print(total)
    
