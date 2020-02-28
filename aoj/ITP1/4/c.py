i=1
while True:
    a, op, b = input().split()
    if op == "?":
        break
    l = a.split()
    if op =="+":
        print(int(a)+int(b))
    if op =="-":
        print(int(a)-int(b))
    if op =="*":
        print(int(a)*int(b))
    if op =="/":
        print(int(a)//int(b))