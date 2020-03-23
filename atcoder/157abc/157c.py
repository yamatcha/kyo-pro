n,m = map(int,input().split())


def judge():
    ans="-"*n
    if m==0:
        if n==1:
            return 0
    for i in range(m):
        s,c = map(int,input().split())
        if ans[s-1]!="-" and int(ans[s-1])!=c:
            return -1
        else:
            a = list(ans)
            a[s-1] = str(c)
            ans = "".join(a)
    if ans[0]=="-":
        a=list(ans)
        a[0]="1"
        ans="".join(a)
    ans=ans.replace("-","0")
    # print(ans[0])
    if ans[0]==str(0):
        if n==1:
            return 0
        else:
            return -1
    return ans

print(judge())