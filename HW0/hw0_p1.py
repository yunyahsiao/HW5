# coding: utf-8
### 還沒打完 我之後會補交的QQ
poly = '(2A+B)(A+B)'.strip(')()').split(')(')
poly2={}
for i in range(len(poly)):
    poly2[i]=poly[i]
poly2
for i in range(len(poly2)):
    for j in range(len(poly2[i])):
        print(poly2[i][j].isalpha())
a=[]
for i in range(len(poly)):
    for j in range(len(poly[i])):
        if poly[i][j] == '+':
            a.append(poly[i].split('+'))
        elif poly[i][j] == '-':
            a.append(poly[i].split('-'))
a
