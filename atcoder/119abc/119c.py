n,a,b,c = map(int,input().split(' '))
l = []
sum=0
for i in range(n):
    l.append(int(input()))

def dfs(sum,std,num):
    now = abs(sum+l[num]-std)
    cond = abs(dfs(sum+l[num],std,num+1)-std)
    if num==n:
        return now
    if now>cond:
        return now
    else:
        return cond

for i in range(n):
    append(dfs(0,a,i)
for i in range(n):
    append(dfs(0,b,i)
for i in range(n):
    dfs(0,c,i)