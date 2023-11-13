stu_name=["a","b","c","d","a"]  #insert duplicate
repeat=0
che_name=input("enter a name :")
for i in range(len(stu_name)):
    if(che_name==stu_name[i]):
      stu_name[i]="anamika"
      repeat=1
if (repeat==0):
    stu_name.insert(1,"amal")
print(stu_name)


#duplicate remove
