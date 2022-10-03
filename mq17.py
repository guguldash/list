str = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
d=0
str1=0
while i<len(str):
    c=0
    for item in str:
        if str[i] == item:
            c=c+1
    if str[i] not in str1:
        str1=str[i]
        d=c
        print(str1, d)     