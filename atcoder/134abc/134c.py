n = int(input())
first=(0,0)
second=0
for i in range(n):
    num = int(input())
    if num>= first[0]:
        second = first[0]
        first=(num,i)
    elif num>=second:
        second = num
# print(n)
for i in range(n):
    if i==first[1]:
        print(second)
    else:
        print(first[0])