n = int(input())
sum=0
dig = len(list(str(n)))
# print(dig)
for i in range(1,dig+1):
    if i%2==1:
        if i==dig:
            sum+=(n-10**(i-1)+1)
        else:
            sum+=10**(i-1)*9

print(sum)