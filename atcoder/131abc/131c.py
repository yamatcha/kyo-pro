import math

a,b,c,d = map(int,input().split())
mul = c*d//math.gcd(c,d)
sum = b//c +b//d -b//mul-a//c-a//d+a//mul
# print(a//c)
# print(sum)
if a%c==0:
    sum+=1
if a%d==0:
    sum+=1
if a%mul==0:
    sum+=1
# print(sum)
print(b+1-a-sum)