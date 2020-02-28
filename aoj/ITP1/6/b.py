s={i for i in range(1,14)}
h={i for i in range(1,14)}
c={i for i in range(1,14)}
d={i for i in range(1,14)}

n = int(input())
for i in range(n):
    m, r = input().split()
    r = int(r)
    if m == "S":
        s.discard(r)
    if m == "H":
        h.discard(r)
    if m == "C":
        c.discard(r)
    if m == "D":
        d.discard(r)

for i in s:
    print("S "+str(i))
for i in h:
    print("H "+str(i))
for i in c:
    print("C "+str(i))
for i in d:
    print("D "+str(i))