elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
sum1=0
sum2=0
for element in elements:
    if element % 2 == 0:
        sum1 = sum1 + element
    else: 
        sum2 = sum2 + element
print("odd",sum2)
print("even",sum1)        

     


