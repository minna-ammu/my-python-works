f=open("C:\\Users\\amalj\\OneDrive\\Desktop\\mypython\\listwork\\fileinputoutput\\f_write\\users\\data.txt","r")
users=[]
for u in f:
    us=u.rstrip("\n")
    name,followings,followers=us.split(",")
    print(name)
    print(followings)
    print(followers)
