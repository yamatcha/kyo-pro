n = int(input())

l=[]
class ab:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def geta(self):
        return self.a


for i in range(n):
    a1,b1 = map(int,input().split)
    nab = ab(a1,b1)
    l.append(nab)
work(0,l)
def work(n,wo):
    if(wo[0].b>wo[0].a+n and (min(wo,key=geta)+wo[0].a+n<=wo[0].b)):
        work(n,wo)
    else:
        del(0)