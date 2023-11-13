wrd="hello morning"
# print(wrd.capitalize())

wrd1="HELLO MORNING"
# print(wrd1.casefold())

wrd2="pneumonia"
# print(wrd2.count("n"))
# print(wrd.count("l"))

wrd3=wrd1.split(" ")
# print(wrd3)

# wrd4="good,morning,happy,new,year"
# print(wrd4.split(","))

wrd5="hai hello how are you"
# print(wrd5.find("r"))

# print(wrd5.startswith("h"))
# print(wrd5.startswith("mor"))

# print(wrd5.endswith("you"))

# print(wrd5.isalpha())
# print(wrd2.isalpha())

# wrd6="hello75"
# print(wrd6.isalnum())

text="one 100 and fifty 5"
txt=text.split(" ")
for ch in txt:
    if(ch.isdigit()):
        print(ch)

# txt=[ ch   for ch in text.split(" ")    if ch.isdigit()]   # using list comprehension
# print(txt)

