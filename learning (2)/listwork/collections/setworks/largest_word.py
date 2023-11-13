word="pneumonoultramicroscopicsilicovolcanoconiosis"
# for ch in word:   # for take each charater from the list
#     print(ch)

vowels={"a","e","i","o","u"}
vow_count=0
cons_count=0
for ch in word:
    if ch in vowels:
        vow_count+=1
    else:
        cons_count+=1
print(cons_count ,"=constn count" ,  "=vowel count" , vow_count)





