# f=open("C:/Users/amalj/OneDrive/Desktop/mypython/listwork/fileinputoutput/data.txt","r")
# for line in f:
#     print(line)





# print("line 1\n")  # idayk vanna gap nokkan...print ne 1 line + enter ne 1 line
# print("line 2")





#  data.text full 1 string ayyitt an kanuka. athine oro words ayitt edukkan an thazhathe method

f=open("C:/Users/amalj/OneDrive/Desktop/mypython/listwork/fileinputoutput/data.txt")
# wrds=[]                  # in case of list
wrds=set()                 # in case of set
for m in f:                # (#$) ippo line il ... hlo hai how do you do...vannu . ivide do kazhinj 
    m=m.rstrip("\n").split(" ")
    # wrd=m.split(" ")     # wrd il ippo 6 words und athine split akknm
    for w in m:
        wrds.add(w)        # wrd ne wrds lott append cheyyan append ...wrds.append(w).....in case of set it is add 
print(wrds) 
# print(set(wrds))         # without using empty  set and add method in set . only final answer 



#    m=m.rstrip("\n")         # (#$) print akumpo \n und line nte end il. means space und . so need to remove space
#    print(m)








