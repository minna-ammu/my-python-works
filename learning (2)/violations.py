from re import *
# violations=["kl-08-av-2794",
#             "KL-08-av-4970",
#             "kl-01-av-14",
#             "kl-01-av-1",
#             "kl-01-av-12",
#             "TN-01-av-1",
#             "ghz-01-avO-1",
#             "0kl-01-av-10"]
# rule="[K][L][-][0-9]{2}[-][a-z]{2}[-][0-9]{1,4}" # {1,4} meaning min 1 max 4
# for m in violations:
#      flmtch=fullmatch(rule,m)
#      if flmtch!=None:
#       print(m,"kerala vehicle") 


tweets="What a game , hats off to both teams . Well done @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"
rule="[@][a-zA-z0-9_]+"        # + means minimum 1 time has to done this rule
flmtch=finditer(rule,tweets) 
for n in flmtch:
     print(n.group())