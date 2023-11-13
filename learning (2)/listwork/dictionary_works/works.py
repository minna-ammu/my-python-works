data={
    "django":"framework",
    "react":"library",
    "fastapi":"framework",
    "vue":"framework",
    "ajax":"library"
    }

       # output frmwrk=3 and lbry=2

# dta={}
# for v in data.values():
#     if v in dta:
#         dta[v]+=1
#     else:
#        dta[v]=1
# print(dta)

       
        # output ={"framework":["django" ,"fatapi","vue"],"library":["ajax","react"]}

dtm={}
for k,v in data.items():
    if v in dtm:
        dtm[v].append(k)
    else:
        dtm[v]=[k]
print(dtm)
