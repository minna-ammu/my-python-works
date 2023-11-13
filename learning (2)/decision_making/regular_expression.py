text="joel is the best student in may"
# txt=text.split(" ")
# print(txt)
# # if txt[0]=="joel":                           # using if 4,5
# #     print("sentence starts with 'joel' ")

# txt2=text.startswith("joel")                   # another method          
# print(txt2)
# if txt2==True:
#     print("sentence starts with 'joel' ")


import re
                                     
# txt=re.search("^joel",text)             # using regular expressio startswith
# print(txt)

# txt2=re.search("in$",text)              # using regular expression endswith
# print(txt2)

txt3=re.search("^joel.*may$",text)        # both starswith and endswith in same sentence
print(txt3)                                
                                          # space also considered 
