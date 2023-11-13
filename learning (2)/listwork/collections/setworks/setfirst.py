# st=set()
# print(st)

# st={90,67,True,"hello",89,11}
# print(st)

# s={78,90,33,56,True}
# for m in s:
#     print(m)

# st={67,78,89,90}
# st.add(44)
# print(st)

# lst=[67,78,True,90,"haii"]    #convert list into set
# st=set(lst)
# print(st)

# s1={78,90,56,45,67}
# s2={12,34,56,78,90}

# un_st=s1.union(s2)             # to make 2 set into one
# print(un_st)

# int_st=s1.intersection(s2)     # common element find
# print(int_st)

# drnt_st=s1.difference(s2)        # to remove elements from first set to second set(s1-s2)
# print(drnt_st)

# lis=[78,89,33,56,90,90,11,56,78] 
# st=set(lis)                      #list il ninne same elements remove cheyyan
# print(st)

all_users=["mohan","ram","roy","tom","umesh","keerthi"]
tom_frnd=["ram","keerthi","umesh"]
keerthi_frnd=["mohan","ram","umesh","roy"]

# frnd_sgst=set(all_users).difference (set(tom_frnd)) #1
# frnd_sgst.remove("tom")
# print(frnd_sgst)

cmn_frnd=set(tom_frnd).intersection(set(keerthi_frnd))#2
print(cmn_frnd)
