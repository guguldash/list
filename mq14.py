elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
c=0
c1=0
while i<len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
        c=c+1
        print("even",elements[i])
    else :
        sum1=sum1+elements[i]
        c1=c1+1
    print() #
    #mq14     
