n = int(input())
v = list(map(int,input().split()))

v = sorted(v)
# print(v)
def dfs (l):
    if len(l)==1:
         return l[0]
    num = (l[0]+l[1])/2.0
    l = l[2:]
    # print(l)
    l.append(num)
    # print(l)
    l = sorted(l)
    return dfs(l)



print(dfs(v))