import itertools

n = int(input())
l = map(int,input().split())
count = 0

l = sorted(l)

# l = list(itertools.combinations(l,3))
# # print(l)

# for i in l:
#     if i[0]+i[1]<i[2] :
#         continue
#     if i[0]+i[2]<i[1] :
#         continue
#     if i[1]+i[2]>i[0] :
#         count+=1
# print(count)