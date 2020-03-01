def judacgt(c):
    return c=="A" or c=="G" or c=="C" or c=="T"


s = input()

max = 0

for i in range(len(s)):
    if judacgt(s[i]):
        if max==0:
            max=1
        for j in range(i+1,len(s)):
            # print(s[i:j])
            if judacgt(s[j])==False:
                break
            elif j-i+1 > max:
                max=j-i+1
print(max)
