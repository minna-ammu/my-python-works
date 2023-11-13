n1=1
n2=34
odd_sum=0
even_sum=0
for i in range(n1,n2):
    if(n1%2==0):
        even_sum+=n1
    else:
        odd_sum+=n1
print("odd sum" ,odd_sum)
print("even sum", even_sum)


