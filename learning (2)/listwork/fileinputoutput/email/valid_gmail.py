from re import *
f=open("C:\\Users\\amalj\\OneDrive\\Desktop\\mypython\\listwork\\fileinputoutput\\email\\data.txt","r")
valid_email=set()      # set because unique
rule="[a-zA-Z0-9][a-zA-Z0-9_$#]*[@]gmail[.]com"    # spcl chrtr akumpo - venadnn thoonunnu
for gm in f:
    gm=gm.rstrip("\n")
    mtch=fullmatch(rule,gm)
    if mtch!=None:
        valid_email.add(gm)
print(valid_email)
