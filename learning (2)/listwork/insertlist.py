# first=[2,3,4,6,7,8]
# first.insert(3,9)
# print(first)

# emptlst=[]
# length=int(input("enter the size of the list :"))
# for i in range(length):
#     num=int(input(f"enter {i}th position  element : ")) 
#     emptlst.append(num)
# maxim=max(emptlst)
# emptlst.insert(2,maxim+10)
# print(emptlst)

stu_name=[]
lenth=int(input ("enter the size of the list :"))
for i in range(lenth):
    name=input(f"enter {i}th name :")
    stu_name.append(name)
# print(stu_name)
chk_name=input("enter a name :")

for s in range(lenth):
    if(stu_name[s]==chk_name):
        stu_name[s]="anamika"
        break
    elif(s==lenth-1):
        stu_name.insert(1,"amal")
print(stu_name)

