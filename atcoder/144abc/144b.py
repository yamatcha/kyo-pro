n = int(input())
flag=False
for i in range(1,10):
    if n%i==0 and 1<=n/i and n/i<10:
        flag=True
print("Yes") if flag==True else print("No")