n = int(input())
cnt = 0
for i in range(n):
    s = str(i)
    if (s.find('7') != -1) and (s.find('5') != -1) and (s.find('3') != -1):
        if s.replace('7','').replace('5','').replace('3','') == '':
            cnt+=1
print(cnt)