# list=[3,45,67,89,99,102]
# element=67
# is_found=False
# for i in range(0,len(list)):
#     if element==list[i]:
#         is_found=True
#         break
        
# print("found" if is_found==True else "not found")
        
list=[23,33,34,56,78,89,203]
lower=0
upper=len(list)-1
element=90
is_found=False
while(lower<=upper):
    mid=(upper+lower)//2
    if element==list[mid]:
        is_found= True
        break

    elif(element<list[mid]):
        upper=mid-1
        
    elif(element>list[mid]):
        lower=mid+1
print("found " if is_found==True else "not found")

