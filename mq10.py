marks=[[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
for mark in marks:
    count=0
    sum=0
    for j in range(len(mark)):
        count=count+1
        sum = sum + mark[j]
    print(sum/count)    
    #avg


    
