import re
# text="hhhhhyyttttkkoooddddwWwwww"
# txt=re.search("[h]{3}",text)
# print(txt)

# text2="zxcvbn45673ffghh6"
# txt2=re.search("[a-z]{6}",text2)
# print(txt2)


# text3="wghtybnTYUIOOP78554ghhyt"
# txt3=re.search("[A-Z]{5}[a-z]]{4}",text3)  # none . because small, capital positons changed
# print(txt3)
text4="ASDFGrtyuuSDF6798jkkkll"
txt4=re.search("[a-z]{4}[A-Z]{3}",text4)     # small letter adhyam pinne capital 
print(txt4)











# regular expression 2 mobile number

# mob=input("your mob num : ")
# num=re.search("^[+]91 [0-9]{10}",mob)
# if num:
#     print("valid mob num")
# else:
#     print(" not valid mob num")
    