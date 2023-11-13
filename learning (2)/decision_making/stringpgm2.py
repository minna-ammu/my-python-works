text="England promised to continue its aggressive approch to test cricket"
text1=text.casefold()             # words starting with vowels
txt=text1.split(" ")
vwls="a","e","i","o","u"
for ch in txt:
    if ch.startswith(vwls):
        print(ch)

# txt2=[ ch   for ch in txt   if  ch.startswith(vwls)]    # using list comprehension
# print(txt2)