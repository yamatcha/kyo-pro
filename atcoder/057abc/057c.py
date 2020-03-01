import math

n = int(input())

def f(a,b):
    return len(str(a)) if len(str(a)) > len(str(b)) else len(str(b))

min = 10

for i in range(1,int(math.sqrt(n))+1):
    if n%i==0 and min > f(i,n//i):
        min = f(i,n//i)

if n<10:
    min=1

print(min)