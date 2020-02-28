n = int(input())
train = 1
for i in range(1,n+1):
    train = train*i%(10**9+7)
print(train)