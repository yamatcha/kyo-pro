s=input()
y,m,d=map(int,s.split('/'))
if y<=2019 and m<=4 and d<=30:
    print('Heisei')
else:
    print('TBD')