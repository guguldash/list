num = [50, 40, 23, 70, 56, 12, 5, 10, 7]
max=0
max2=0
for item in num:
    if item > max:
        max2=max
        max = item
    if max2 < item < max:
        max2 = item
# print(max,"is maximum" )
print(max2,"is maximum")
