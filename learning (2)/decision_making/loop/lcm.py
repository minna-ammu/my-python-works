n1=12
n2=24
lcm=1
for i in range(1,13):
    if(n1%i==0) and (n2%i==0):
        hcf=i
lcm=(n1*n2)/hcf
print(lcm)