import sys
sys.setrecursionlimit(10**6)

readline = sys.stdin.readline

n,q = map(int,readline().split())
a=[[] for i in range(n)]
l=[0]*n
ans=[0]*n

def dfs(parent,current,value):
    value += l[current]
    ans[current] = value
    for i in a[current]:
        if i != parent:
            dfs(current,i,value)


for i in range(n-1):
    t1,t2 = map(int,readline().split())
    a[t1-1].append(t2-1)
    a[t2-1].append(t1-1)
    
for i in range(q):
    t1,t2 = map(int,readline().split())
    l[t1-1]+=t2
dfs(-1,0,0)

print(" ".join(map(str,ans)))