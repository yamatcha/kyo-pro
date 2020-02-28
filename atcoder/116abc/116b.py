def f(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1
        
s = int(input())

cnt=1
l = []
j=False
while j==False:
    if s in l:
        print(cnt)
        j=True
    l.append(s)
    s = f(s)
    cnt+=1
