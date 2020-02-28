n,m = map(int,input().split())
data = []
sum=0


for i in range(0,n):
    a,b = map(int,input().split())
    data.append((a,b))

data.sort()

while m>0:
    num = m if m<data[0][1] else data[0][1]
    sum+=data[0][0]*num
    m-=num
    del data[0]

print(sum)

