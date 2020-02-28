n = int(input())
a = list(map(int,input().split()))

sum = 0
for i in a:
    sum+=1.0/i

print(1.0/sum)