# import  re
# text="hlo hai  good morng how are u all "
# txt=re.sub(" ",",",text)
# print(txt)

# from re import *
# text="jklrtiijkl5677dffejkl990jkl455"
# count=0
# txt=finditer("jkl",text)
# for t in txt:
#     print(t.start())
#     # print(t.group())
#     count+=1
# print(count)


# text2="luminar lab lab techno luminar lab luminar "
# txt2=finditer("lab",text2)   
# count=0
# for t in txt2:
    # print(t.group())
    # print(t.start())
    # count+=1
# print(count)
# print(type(txt2))


                               
# text3="G9H5kj7y9u C8g3d45hj67"
# tx3=finditer("[C-H]",text3)             # [l-r] from l to r and [A-N] capital a to n
# txt3=finditer("[3-6]",text3)             # all alphabets [-] ,[0-9]
# for t in tx3:
#     print(t.start())
# for tt in txt3:
#     print(tt.start())

# text4="b$hhDG*YU 67GH 90n%njh$"
# txt4=finditer("[^a-zA-Z0-9]",text4)    # special characters print cheyyan
# for t in txt4:
#     print(t.group())
#     print(t.start())

# (a-z)  = /w            (0-9) = /d              (space)= /s

#  exclude (a-z) =/W     exclude digits=/D       space exclude =/S

# from re import *

# rule="[k-m][369][a-zA-Z0-9]*"       # sample rule
# varbl="k9ght67"
# v=fullmatch(rule,varbl)    
# if v!=None:
#     print("it is valid")
# else:
#     print("it is invalid")

# from re import *
# rule="[A-Za-z_][a-zA-Z0-9]*"          # rule for python variable
# varble="mkkko"
# flmtch=fullmatch(rule,varble)
# if flmtch==None:
#     print("not matched")
# else:
#     print("fully matched")

# from re import *
# rule="[A-Za-z][A-Za-z0-9_$]{0,10}"    # rule for java  , {n1,n2} for quantity by using comma  
# varble="u"
# flmatch=fullmatch(rule,varble)
# if flmatch==None:
#     print("not matched")
# else:
#     print("fully matched")

# from re import *
# rule="[K][L][-][0-9]{2}[-][a-z]{2}[-][0-9]{4}"  # rule for kerala vehicle note kl
# varble="KL-78-gh-7906"
# flmatch=fullmatch(rule,varble)
# print("fully matched" if flmatch!=None else "not matched")



