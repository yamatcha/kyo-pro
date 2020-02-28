s = list(input())
min = 10000
#print(s)
for i in range(1,len(s)-1):
    li = list(map(int,s[i-1:i+2]))
  #  print(li)
    num = li[0]*100+li[1]*10+li[2]
 #   print(num)
    if abs(753-num) < min:
        min = abs(753-num)

print(min)