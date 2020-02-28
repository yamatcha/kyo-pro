n = int(input())
h=list(map(int,input().split()))
def jud(n,h):
    for i in list(reversed(range(0,n-1))):
        # print(h[i],h[i+1])
        if h[i+1]-h[i]==-1:
            h[i]-=1
            # print(h[i])
            continue
        if h[i]-h[i+1]>1:
            return "No"
            break
    return "Yes"

print(jud(n,h))
