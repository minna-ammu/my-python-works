weight_kg=67
height_cm=160
height_m=height_cm/100 #160/100=1.6
bmi=weight_kg/height_m**2
print(bmi)

if(bmi<=18.5):
    print("under weighted")
elif(bmi<=24.9):
    print("normal weight")
elif(bmi<=29.9):
    print("over weight")