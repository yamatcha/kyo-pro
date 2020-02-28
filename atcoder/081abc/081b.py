n = int(input())
a = list(map(int,input().split()))
cnt = 0

while True:
    jud = True
    for i,b in enumerate(a):
        if b%2==1:
            jud = False
        a[i]/=2
    if jud==False:
        break
    cnt+=1
print(cnt) 
