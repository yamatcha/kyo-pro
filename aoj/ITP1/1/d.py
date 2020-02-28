x = int(input())
l = []
l.append(x//60)
l.append(x%60)
l.append(l[0]//60)
l[0] = l[0]%60 
m,s,h = map(str,l)
print(h+":"+m+":"+s)