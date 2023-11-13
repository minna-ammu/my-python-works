# text="pneumonoultramicroscopicsilicovolcanoconiosis"

# wc={}
# for ch in text:
#     if ch in wc:
#         print(ch, "is first recursive character")
#         break
#     else:
#         wc[ch]=1

# word count
wrds=["hello","hai","hello","hai","good","morning","evening"]
wd={}
for w in wrds:
    if w in wd:
        wd[w]+=1
        
    else:
         wd[w]=1
print(wd)




