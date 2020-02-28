n = int(input())
h = list(map(int,input().split()))
a = [0]
for i in reversed(range(len(h)-1)):
    if h[i]>=h[i+1]:
        a.append(a[len(a)-1]+1)
    else:
        a.append(0)
# print(a)
print(max(a))