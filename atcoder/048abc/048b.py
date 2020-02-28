def f(i,x):
   if i == -1:
        return 0
   else:
        return i//x+1

a, b, x = map(int,input().split())
cnt = f(b,x)-f(a-1,x)

print(cnt)
    
