list=[[34,56],[78,65],[90,65]]
# for sublst in list:
#     for num in sublst:
#         print(num)

# for sblst in list:
#     for num in sblst:
#         if num>50:
#             print(num)


#list comprehension in nested list

# allnum=[ num for sublst  in list for num in sublst ]
# print(allnum)

n_gtr_50=[n for sblst in list for n in sblst if n>50]
print(n_gtr_50)
