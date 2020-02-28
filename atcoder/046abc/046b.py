n,k = map(int,input().split())

c = k

for i in range(n-1):
    c *= k-1

print(c)
    
