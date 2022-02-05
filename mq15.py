


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
c=0
c1=0
c2=0
sum=0
sum1=0
sum2=0
i=0
while i<len(elements):
    c=c+1
    sum=sum+elements[i]
if elements[i]%2==0 :
    c=c+1
    sum=sum+elements[i] 
else:
    c2=c2+1
    sum2=sum2+elements[i] 
i=i+1
print("total count",c) 
print("even number",c1)
print ("odd number",c2)
print("total sum",sum)
print("even number",sum1)
print("odd number",sum2)
print("total average",sum/c)
print("even number",sum1/c+1)
print("odd number",sum2/c2)

    

