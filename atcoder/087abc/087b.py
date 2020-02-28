l = list(map(int,input().split()))
cnt = 0

for i in range(0,l[0]+1):
    for j in range(0,l[1]+1):
        for k in range(0,l[2]+1):
            if 500*i+100*j+50*k==l[3]:
                cnt+=1

print(cnt)


