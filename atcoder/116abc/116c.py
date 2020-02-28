n = int(input())
h = list(map(int,input().split))

l = [0]

for i in range(0,n-1):
    if h[i] <= h[i+1]:
        l[cnt]=i+1
    else: 
        l.append(i+1)
        cnt+=1
print(l)
