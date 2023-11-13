n=3456
org=n
cnt=len(str(n))
sum=0
while(n!=0):
    digit=n%10
    sum=sum+digit**cnt
    n=n//10
if(sum==org):
    print("armstrong number")
else:
    print("not armstrong number")
