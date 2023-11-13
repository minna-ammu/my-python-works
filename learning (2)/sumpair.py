# list=[2,3,4,5]
# sum=8
# cur_sum=0
# for i in list:
#     for j in list:
#         if(i!=j) and (i<j):
#             cur_sum=i+j
#             if(cur_sum==sum):
#                 print(i,j)


list=[2,3,4,5,6,7,8]
upper=len(list)-1
lower=0
sum=11
while (lower<upper):
    crnt_sum=list[lower]+list[upper]
    if (crnt_sum==sum):
        print("pairs",list[lower],list[upper])
        lower+=1       # not use break use lower+=1 because in case of break 1 pair 
    elif(crnt_sum<sum):
        lower+=1
    elif(crnt_sum>sum):
        upper-=1
    

