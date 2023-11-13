from re import *
f=open("C:/Users/amalj/OneDrive/Desktop/mypython/listwork/fileinputoutput/vehicle/data.txt","r")
st1_k=set()
st2_t=set()
rule_t="[T][N][-][0-9]{2}[-][A-Z]{1}[-][0-9]{4}"
rule_k="[K][L][-][0-9]{2}[-][A-Z]{1}[-][0-9]{4}"

for v in f:
    v=v.rstrip("\n")
    mtch1=fullmatch(rule_k,v)
    mtch2=fullmatch(rule_t,v)
    if mtch1!=None:
        st1_k.add(v)
    elif mtch2!=None:
        st2_t.add(v)
print("kerala vehicle" ,st1_k)
print("tamilnadu vehicle",st2_t)





