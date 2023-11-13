# list1=[12,13,17,46,89,70]
# list2=[34,80,13,45,12,57]
# for n1 in list1:
#     for n2 in list2:
#         if(n1==n2):
#             print(n1)


#algorithm (sorted list only)

# list1=[11,19,37,48,91,98]
# list2=[19,23,44,67,90,91]
# p1=0
# p2=0

# while (p1<len(list1) and p2<len(list2)):
#     if(list1[p1]==list2[p2]):
#         print(list1[p1])
#         p1+=1
#     elif(list1[p1]<list2[p2]):
#         p1+=1
#     elif(list1[p1]>list2[p2]):
#         p2+=1


#duplicate from 1 list
list=[2,3,4,4,7,8,11,11,24]
for i in list:
     if( list[i]==list[i+1]):
            print(list[i])
