list=[2,3,4,6,9]

for i in range(0,len(list)):
    elemt1=list[i]
    elemt2=list[i+1]

    if(elemt2-elemt1 !=1):
        print(elemt1+1)
        elemt1+=1
        break


