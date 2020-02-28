a,b = map(int,input().split(" "))
plus = a+b
sub = a-b
mul = a*b
max = plus if plus>sub else sub
max = mul if mul>max else max
print(max)