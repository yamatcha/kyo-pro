n,m,k = map(int,input().split())
l=[[] for i in range(n)]
print(l)
for i in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    l[a].append(b)
    l[b].append(a)
print(l)
seen = [False for _ in range(n)]

def dfs(g, v):
    seen[v]=True
    for next in g[v]:
        if seen[next]:
            continue
        dfs(g,next)

count=0

for v in range(n):
    if seen[v]:
        continue
    dfs(l,v)
    count+=1

for i in range(k):
    c,d = map(int,input().split())