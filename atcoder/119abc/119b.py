n = int(input())

sum=0

for i in range(n):
    m,k = input().split(' ')
    m = float(m)
    if k=='BTC':
        m*=380000.0
    sum+=m

print(sum)