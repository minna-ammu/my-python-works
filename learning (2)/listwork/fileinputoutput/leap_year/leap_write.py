# f=open("C:\\Users\\amalj\\OneDrive\\Desktop\\mypython\\listwork\\fileinputoutput\\leap_year\\data.txt","w")
# years=[2000,2024,1992,1991,1995,1400,1567,2980]
# for y in years:
#     if (y%100==0 and  y%400==0):   # century year anon ariyan 100, if century then 400 for laep year
#         f.write(str(y)+"\n")
#     elif(y%100!=0 and y%4==0):     # century year allenkl leap year ne 4
#         f.write(str(y)+"\n")
# print("finished")

    
f=open("C:\\Users\\amalj\\OneDrive\\Desktop\\mypython\\listwork\\fileinputoutput\\leap_year\\sample_year.txt","w")
for n in range(1890,3001):     # 3000 vare kittan 3001 koduthu.
    f.write(str(n)+"\n")
print("finished")