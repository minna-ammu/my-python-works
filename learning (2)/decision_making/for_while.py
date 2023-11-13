n=1634
cnt=len(str(n))
sum=0
while(n!=0):
   digit=n%10  
   sum=sum+digit**cnt
   n//10     
print(sum)