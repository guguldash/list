number=30
n=[10,11,12,13,14,17,18,19]
i=0
l=[]
while i<len(n):
	j=i
	while j<len(n):
		c=n[i]+n[j]
		if c==30:
			d=[n[i],n[j]]
			l.append(d)
		j+=1
	i+=1
print(l)
# Output
# [[11, 19], [12, 18], [13, 17]]

