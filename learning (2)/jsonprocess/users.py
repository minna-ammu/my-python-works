from json import load
# f=open("C:\\Users\\amalj\\OneDrive\\Desktop\\mypython\\jsonprocess\\data.json","r")
# dta=load(f)
# # print(dta)
# f.close()

with open("C:\\Users\\amalj\\OneDrive\\Desktop\\mypython\\jsonprocess\\data.json","r") as f:
 dta=load(f)                       # close cheyyan eluppathine ulla vazhi
#  print(dta)

# for u in dta:
#     print(u.get("name"))         # ellarudeyum name print cheyyan *


# nms=[u.get("name") for u in dta]   # using list comprehension *
# print(nms)

# cndte=max(dta,key=lambda s:s.get("total"))  # maximum score kanan
# print(cndte)

# srt=sorted(dta,reverse=True,key=lambda s:s.get("total"))
# print(srt)                             # marks nte decending order il sort cheyyan


bca_stdnt=[ u.get("name")     for u in dta       if u.get("course")=="bca"]
print(bca_stdnt)                # bca student nte name print cheyyan
