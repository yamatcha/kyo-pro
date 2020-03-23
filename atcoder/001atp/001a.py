import sys
sys.setrecursionlimit(10**7)

h,w = map(int,input().split())
c = []
for i in range(h):
    c.append(list(input()))

seen = [[False]*w for i in range(h)]

def dfs(i,j):
    seen[i][j]=True
    # print(i,j)
    if c[i][j]=="g":
        return 
    if i>0 and seen[i-1][j]==False and c[i-1][j]!="#":
        dfs(i-1,j)
    if i<h-1 and seen[i+1][j]==False and c[i+1][j]!="#":
        dfs(i+1,j)
    if j>0 and seen[i][j-1]==False and c[i][j-1]!="#":
        dfs(i,j-1)
    if j<w-1 and seen[i][j+1]==False and c[i][j+1]!="#":
        dfs(i,j+1)
    return
gi=0
gj=0
for i in range(h):
    if 's' in c[i]:
        dfs(i,c[i].index("s"))
    if 'g' in c[i]:
        gi=i
        gj=c[i].index("g")
if seen[gi][gj]==True:
    print("Yes")
else:
    print("No")
# print(seen)