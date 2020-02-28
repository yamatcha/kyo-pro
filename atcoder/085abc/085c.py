n = int(input())
y = int(input())

bills = [1000,5000,10000]
def gety():
    for i in range(n):
        for j in range(n-i):
            k = n-i-j
            if i*1000+j*5000+k*10000==y and i+j+k==n :
                return [i,j,k]

print(gety())