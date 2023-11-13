words=["good","hai","in","bad","koolie","a","pneumonia"]
# print(min(words,key=lambda w:len(w)))
# print(max(words,key=lambda w:len(w)))

srt=sorted(words,reverse=True,key=lambda w:len(w))
print(srt)


# num=[23,44,89,21,20,56,11]
# print(sorted(num,reverse=True))