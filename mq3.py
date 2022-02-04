num = [50, 40, 23, 70, 56, 12, 5, 10, 7]
max=0
i=0
max2=0
while i<len(num):
    if num[i]>max:
        max2=max
        max=num[i]
    if max2<num[i]<max:
      max2=num[i]  
    i=i+1
# print(max,"is maximum" )
print(max2,"is maximum")
