h,w = map(int,(input().split()))
li = []
jud = 1
for i in range(h):
    li.append(list(input()))
dx = [0,1,-1,0]
dy = [1,0,0,-1]
num = 0
for i in range(h):
    for j in range(w):
        if li[i][j] == '#':
            num=0
            for d in range(len(dx)):
                ni = i+dy[d]
                nj = j+dx[d]
                if ni < 0 or h <= ni:
                    continue
                if nj < 0 or w <= nj:
                    continue
                if li[ni][nj] == '#':
                    num+=1
            if num == 0:
                jud = 0
                break

if jud == 0:
    print("No")
if jud == 1:
    print("Yes")
            
        