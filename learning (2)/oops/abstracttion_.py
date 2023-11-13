class P1:
    def m1 (self):
        print("p1 and m1 are in  same league")

class P2:
    def m1 (self):            # first use m2 then second time use same as m1
        print("p2 and m2 are in same league")


class K1(P1,P2):
    pass

u=K1()
u.m1()
# u.m2()