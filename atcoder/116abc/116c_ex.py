n = int(input())
h = list(map(int,input().split()))

l = [0]
cnt=0
sum=0

for i in range(n-1):
    if h[i]<=h[i+1]:
        l[cnt]=(i+1)
    else:
        l.append(i+1)
        cnt+=1
if h[n-1]<h[n-2]:
    l.remove(n-1)

for i in range(len(l)-1):
    mi =  h[l[i]] 
    for j in range(l[i],l[i+1]):
        if mi > h[j]:
            mi=h[j]
    sum+=h[l[i]]-mi

print(sum+h[l[len(l)-1]])
