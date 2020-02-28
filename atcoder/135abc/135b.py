n = int(input())
p = list(map(int,input().split()))

s=sorted(p)
cnt=0

def jud(p,s,n,cnt):
    # print(p,s)
    for i in range(n):
        if s[i]!=p[i]:
            cnt+=1
        if cnt>2:
            return "NO"
    return "YES"

print(jud(p,s,n,cnt))