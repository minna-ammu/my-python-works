# addition=lambda n1,n2 :n1+n2
# print(addition(19,78))

# substn=lambda n,m :n-m
# print(substn(88,34))

# multptn=lambda j,m: j*m
# print(multptn(87,21))

# dvtn=lambda o,p:o/p
# print(dvtn(89,13))

# student={"roll":67, "name":"hansuk","course":"it"}
# def get_name(stdnt):
#     return stdnt.get("name")
# print(get_name(student))

employee={"id":98,"name":"madhavi","salary":67000,"positon":"hr"}
# def name(nme):
#     return nme.get("name")
# print(name(employee)) 

# name=lambda nme:nme.get("name")    # in lambda above
# print(name(employee)

# def salary(slry):
#     return slry.get("salary")
# print(salary(employee))

salary=lambda slry:slry.get("salary") # in lambda above
print(salary(employee))