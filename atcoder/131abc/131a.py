s = list(input())
# print(s)
cnt=0
flag=0
for i in s:
    if cnt==0:
        cnt+=1
        pre=i
        continue
    else:
        if pre==i:
            flag=1
            # print("hoge")
    pre = i
    cnt+=1 
    # print(cnt)
if flag==0:
    print("Good")
else:
    print("Bad")

