wrd="supervsior"
input="superior"
wc={}
is_kangaroo_word=True
for w in wrd:
    if w in wc:
       wc[w]+=1
    else:
        wc[w]=1
# print(wc)
for m in input:
    if m in wc and wc[m]>0:
        wc[m]-=1
    else:
        is_kangaroo_word=False
        break
print(is_kangaroo_word)
