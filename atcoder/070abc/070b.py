a,b,c,d = map(int,input().split())
s = max(a,c)
f = min(b,d)
time = f-s
if time < 0:
    time = 0 
print(time)