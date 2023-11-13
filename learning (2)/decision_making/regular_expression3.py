sent=" 54 hlo hi 46  good hi 48 hlo 34 hlo 55 hidden 18:5 eveng hi 34,5 hlo 45 hide 67 hlo "
# cnt=sent.count("hi")
# print(cnt)

import re
# cnt=re.findall("hi",sent)
# print(len(cnt))


nums=re.findall("[0-4][0-6]",sent)    # first letter between 0-4 and second letter betwn 0-6
print(nums)


# verify the gmail account

# gmail=input("enter your gmail id : ")
# g=re.search("@gmail.com$",gmail)
# if g :
#     print("it is valid ")
# else:
#     print("not valid")
