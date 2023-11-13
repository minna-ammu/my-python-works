n1=100
n2=125
n3=80

first = 0
second =0
third =0

if((n1>n2) and (n1>n3)):
    first=n1
    if(n2>n3):
        second=n2
        third=n3
    else:
        second=n3
        third=n2
elif((n2>n1) and (n2>n3)):
    first=n2
    if(n1>n3):
        second=n1
        third=n3
    else:
        second=n3
        third=n1
elif((n3>n1) and (n3>n2)):
    first=n3
    if(n1>n2):
        second=n1
        third=n2
    else:
        second=n2
        third=n1
print(first,second,third)