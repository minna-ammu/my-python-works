for row in range(1,5):
    for col in range(1,8):
        if(row==1) or (row==col) or (col+row==8):
            print("*" ,end="")
        else:
            print(end=" ")
    print()
