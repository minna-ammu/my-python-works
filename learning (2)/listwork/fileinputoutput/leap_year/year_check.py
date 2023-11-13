f_read=open("C:/Users/amalj/OneDrive/Desktop/mypython/listwork/fileinputoutput/leap_year/sample_year.txt","r")
f_write=open("C:\\Users\\amalj\OneDrive\\Desktop\\mypython\\listwork\\fileinputoutput\\leap_year\\sample_year_check.txt","w")
for y in f_read:                 # 1890 y il varum ippo wih \n  like("1890\n"). so  \n ne remove cheyynm
    year=int(y.rstrip("\n"))     # y ne rtsrip cheyyumpo string an kituka. so athine integer lott mattnm 
    if(year%100==0 and year%400==0):
        f_write.write(str(year)+"\n")
    elif(year%100!=0 and year%4==0):
        f_write.write(str(year)+"\n")


