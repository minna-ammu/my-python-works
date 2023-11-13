f1=open("C:\\Users\\amalj\\OneDrive\\Desktop\\mypython\\listwork\\dictionary_works\\attendence\\total.present")
f2=open("C:\\Users\\amalj\\OneDrive\\Desktop\\mypython\\listwork\\dictionary_works\\attendence\\today.present")
ts_st=set()
ps_st=set()
for m in f1:
    ts_st.add(m.rstrip("\n"))
# print(ts_st)
for n in f2:
    ps_st.add(n.rstrip("\n"))
    # ab_st=ts_st.difference(ps_st)
    ab_st=ts_st-ps_st
print(ab_st)




