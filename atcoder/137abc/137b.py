k,x = map(int,input().split(" "))
result = " ".join(map(str,list(range(x-k+1,x+k))))

print(result)