from ast import While


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
c=0
c1=0
for element in elements:
    if element % 2 == 0:
        c=c+1
    else:
        c1=c1+1
print(c,'even')
print(c1,"odd")  
#evn od count

        


