list=[78,89,90,86,43,67]
# a=76
# if a in list:
#     print("76 is present")
# else:
#     print("76 is not present")

# if 88 not in list:
#     print("88 is not present")
# else:
#     print("88 is  present")


# cars=["lamborgini","maruthi800","bmw","porche"]
# car_o=[]
# for c in cars:
#     if "o" in c:
#         car_o.append(c)
# print(car_o)


# n=[3,4,5,6,8.9,1]
# n.pop(1)
# print(n)
# n.pop(3-1)
# print(n)
# n.pop(4-2)
# print(n)

# n=[60,88,90,67,54,55,43,32,10,15]
# n1=[]
# for num in n :
#   if (n%5==0) and (n%2!=0):
#     n1.append(n)
# print(n1) 

lst=[23,34,54,43]
mini=lst[0]
for n in lst:
    if mini>n:
        mini=n
        c=lst.pop(mini)
print(mini)
print()


