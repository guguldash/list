from ast import Not


list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
a = [item for item in list1 if item not in list2]
print(a)      