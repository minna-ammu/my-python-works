import re
mob=input("enter your mobile number with country code :")
m=re.search("^[+]91",mob)
if (m):
    print("number is from india")
else:
    print("number is not from india")





# resi=input("enter the residence number")
# erkm=re.search("^0484",resi)
# knnr=re.search("^0460",resi)
# kzkd=re.search("^0490",resi)
# mlprm=re.search("^0487",resi)
# idky=re.search("^0678",resi)
# if erkm:
#     print("ekrm")
# elif knnr:
#     print("knnr")
# elif kzkd:
#     print("kzkd")
# elif mlprm:
#     print("mlprm")
# elif idky:
#     print("idky")