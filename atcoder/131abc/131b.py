n,l = map(int,input().split())

def taste(x,l):
    return x+l-1
tastes=[]
for i in range(1,n+1):
    tastes.append(taste(i,l))
min = 0
cnt=0
for i in range(0,n):
    if abs(tastes[min]) >= abs(tastes[i]):
        min=i
del tastes[min]
# print(min)
# print(tastes)
print(sum(tastes))