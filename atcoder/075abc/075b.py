li = []
a, b = map(int,input().split())
for i in range(a):
    li.append(list(input()))

for i in range(a):
    for j in range(b):
        if li[i][j] == '.':
            li[i][j] = 0
            if i!=0 and li[i-1][j]=='#':
                li[i][j]+=1
            if i!=a-1 and li[i+1][j]=='#':
                li[i][j]+=1
            if j!=0 and li[i][j-1]=='#':
                li[i][j]+=1
            if j!=b-1 and li[i][j+1]=='#':
                li[i][j]+=1
            if i!=0 and j!=0 and li[i-1][j-1]=='#':
                li[i][j]+=1
            if i!=a-1 and j!=0 and li[i+1][j-1]=='#':
                li[i][j]+=1
            if i!=0 and j!=b-1 and li[i-1][j+1]=='#':
                li[i][j]+=1
            if i!=a-1 and j!=b-1 and li[i+1][j+1]=='#':
                li[i][j]+=1
        print(li[i][j],end="")
    print()