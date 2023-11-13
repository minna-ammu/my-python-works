wrd=input("enter a string :")
wrd_2=input("enter another string :")
srt_wrd=sorted(wrd)
srt_wrd_2=sorted(wrd_2)

print(srt_wrd)
print(srt_wrd_2)

print("anagram" if srt_wrd==srt_wrd_2 else "not anagram")