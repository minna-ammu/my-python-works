mobiles=[[100,"nnjyhjkjgj" ,45543,"5g"],
         [101,"mmmmmmmmmm" ,56677,"2g"],
         [102,"nnkhgfdfgh" ,12344,"4g"],
         [103,"iiiiiiiiii" ,54673,"5g"],
         [104,"xxzzxzxxxx" ,9876,"4g"],
         [105,"qweeeerrrr" ,67889,"5g"]]


# print(len(mobiles)) #number of moblies len

# mobile_names=[ mob[1] for mob in mobiles ]
# print(mobile_names)

# fourg_mob=[mob[1] for mob in mobiles if mob [3]=="4g"] # 4g mobile names only
# print(fourg_mob)

# price=[ mob[0]for mob in mobiles if mob[2]>45000]  #45000<mobile nte num like 100,101...
# print(price)

# range_mob=[ m[1]for m in mobiles if m[2]>30000 and m[2]<50000]
# print(range_mob)

mobile=[ m[1] for m in mobiles if m[3]=="5g" and m[2]<55000 ]
print(mobile)
