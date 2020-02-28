from operator import itemgetter
n=int(input())
l=[]
for i in range(1,n+1):
    a,b=input().split()
    t=tuple([a,b,i])
    l.append(t)
b = sorted(l, key=itemgetter(1), reverse=True)
c = sorted(b,key=itemgetter(0))
for i in c:
    print(i[2])