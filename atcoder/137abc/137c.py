import sys
sys.setrecursionlimit(10000000)
nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]

n = int(input())
s=[]
m={}
sum=0
for i in range(0,n):
    # print((list(input()))
    tmp = "".join(sorted(input()))
    if tmp in m:
        m[tmp]+=1
    else:
        m[tmp] = 1
for k in m:
    if m[k]>1:
        # print(m[k])
        # print("["+k)
        sum+=cmb(m[k],2)
print(sum)

