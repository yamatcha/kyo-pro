x=[]
y=[]

while True:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    else:
        if a>b:
            x.append(b)
            y.append(a)
        else:
            x.append(a)
            y.append(b)

for i in range(len(x)):
    print(x[i],y[i])
