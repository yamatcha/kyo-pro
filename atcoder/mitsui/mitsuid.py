# resolve after read answer

n = int(input())
s = input()

# count = 0
# for i in range(1000):
#     v = str(i).zfill(3)
#     k=0
#     for j in range(n):
#         if v[k] == s[j]:
#             k+=1
#         if k==3:
#             count+=1
#             break

# print(count)

# dp
dp = [[[False] * 30009 for i in range(4)] for j in range(1009)]
dp[0][0][0]=True
cnt=0
for i in range(n):
    for j in range(4):
        for k in range(1000):
            if dp[i][j][k] == False:
                continue
            dp[i+1][j][k] = True
            if(j<=2):
                dp[i+1][j+1][k*10+int(s[i])]=True
for i in range(1000):
    if(dp[n][3][i]==True):
        cnt+=1
print(cnt)
