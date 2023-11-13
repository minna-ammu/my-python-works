text="AABBCCCDDEEEE"
                      # most recursive character
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
print(wc)
        
print(min(wc,key=lambda k:wc.get(k)))      
print(max(wc,key=lambda k:wc.get(k)))     