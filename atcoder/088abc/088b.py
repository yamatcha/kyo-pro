n = int(input())
a = list(map(int,input().split()))
suma = 0
sumb = 0

a.sort()
for i,num  in enumerate(a):
    if i%2==0:
        suma+=num
    else:
        sumb+=num 
print(suma-sumb)
