kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
c=0
c1=0
c2=0
i=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>1000000:
        c=c+1
    elif kitna_paisa_hai[i]<1000000 and kitna_paisa_hai[i]  >100000:
        c1=c1+1
    else:
        c2=c2+1
    i=i+1
    print(c,"corodpati hai") 
    print(c1, "lakhpati hai" )
    print (c2,"dilwali hai")  
    #wrong hai 


